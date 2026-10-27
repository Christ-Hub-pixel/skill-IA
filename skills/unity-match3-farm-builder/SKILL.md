---
name: unity-match3-farm-builder
description: Complete Unity game development skill for hybrid Match-3 and Farm simulation games (like Farm Bloom, Gardenscapes, Farm Heroes Saga). Use when designing or coding C# scripts, ScriptableObjects, grid algorithms, match-3 mechanics, tile cascading, boosters, farm plots with growth timers, barn/building upgrade systems with multi-resource requirements, inventory management, and smooth tweening animations.
---

# Unity Match-3 & Farm Builder Architecture

Guide d'ingénierie et catalogue de scripts C# modulaires pour jeux hybrides **Match-3 + Gestion de Ferme** (type *Farm Bloom*, *Gardenscapes*, *Farm Heroes*).

---

## 1. Piliers d'Architecture C# / Unity

1. **Architecture orientée données (Data-Driven avec ScriptableObjects)** :
   * Chaque légume, fruit, culture, booster et niveau est une instance de `ScriptableObject`.
   * Séparation stricte entre les données de configuration (`CropData`, `TileData`, `BuildingUpgradeData`) et les contrôleurs de scène (`MonoBehaviour`).

2. **Système événementiel découplé (Observer Pattern)** :
   * Communication par événements C# `System.Action` pour éviter les dépendances circulaires entre la grille Match-3, la ferme et l'inventaire.

3. **Performance & Zéro Garbage Collection** :
   * **Object Pooling** pour les tuiles de la grille, les particules de récolte et les popups de score.
   * Pas d'allocations mémoire dynamiques dans les boucles `Update()`.

---

## 2. Modèles de Données & ScriptableObjects

### A. Types de Tuiles & Boosters (`TileData.cs`)
```csharp
using UnityEngine;

namespace FarmBloom.Match3
{
    public enum TileType { Carrot, Tomato, Corn, Strawberry, WaterDrop, Wheat }
    public enum SpecialBoosterType { None, LineClearHorizontal, LineClearVertical, Bomb3x3, RainbowWateringCan }

    [CreateAssetMenu(fileName = "NewTileData", menuName = "FarmBloom/Match-3 Tile Data")]
    public class TileData : ScriptableObject
    {
        public TileType tileType;
        public string displayName;
        public Sprite baseSprite;
        public Color tileColor = Color.white;
        public int scoreValue = 50;
        public GameObject matchParticlesPrefab;
    }
}
```

### B. Cultures & Étapes de Pousse (`CropData.cs`)
```csharp
using UnityEngine;

namespace FarmBloom.Farm
{
    [CreateAssetMenu(fileName = "NewCropData", menuName = "FarmBloom/Crop Data")]
    public class CropData : ScriptableObject
    {
        public string cropId;
        public string displayName;
        public Sprite icon;
        [Tooltip("Sprites successifs pour chaque phase visuelle de pousse")]
        public Sprite[] growthStageSprites;
        public float growthDurationSeconds = 120f; // ex: 2 minutes en temps réel
        public int harvestYield = 3;
        public int coinsReward = 25;
        public int xpReward = 10;
    }
}
```

### C. Améliorations de Bâtiment (`BuildingUpgradeData.cs`)
```csharp
using System;
using UnityEngine;

namespace FarmBloom.Buildings
{
    [Serializable]
    public struct ResourceRequirement
    {
        public string resourceId; // "wood", "hammer", "nail", "coins"
        public int amountRequired;
    }

    [CreateAssetMenu(fileName = "NewBuildingUpgrade", menuName = "FarmBloom/Building Upgrade")]
    public class BuildingUpgradeData : ScriptableObject
    {
        public string buildingId; // "Barn", "Silo", etc.
        public int targetLevel;
        public int newStorageCapacity;
        public Sprite upgradedSprite;
        public ResourceRequirement[] requirements;
    }
}
```

---

## 3. Système Match-3 6x6 : Algorithme, Swap & Cascade

### A. Détecteur d'Alignements (`MatchFinder.cs`)
```csharp
using System.Collections.Generic;
using UnityEngine;

namespace FarmBloom.Match3
{
    public class MatchResult
    {
        public HashSet<TileController> MatchedTiles = new HashSet<TileController>();
        public List<Vector2Int> LineOf4 = new List<Vector2Int>();
        public List<Vector2Int> LineOf5 = new List<Vector2Int>();
    }

    public static class MatchFinder
    {
        public static MatchResult FindMatches(TileController[,] grid, int width, int height)
        {
            MatchResult result = new MatchResult();

            // 1. Alignements horizontaux
            for (int y = 0; y < height; y++)
            {
                int matchLength = 1;
                for (int x = 0; x < width; x++)
                {
                    bool isEnd = (x == width - 1);
                    if (!isEnd && grid[x, y] != null && grid[x + 1, y] != null &&
                        grid[x, y].Data.tileType == grid[x + 1, y].Data.tileType)
                    {
                        matchLength++;
                    }
                    else
                    {
                        if (matchLength >= 3)
                        {
                            for (int i = 0; i < matchLength; i++)
                            {
                                int cx = isEnd && (grid[x, y] != null && x > 0 && grid[x, y].Data.tileType == grid[x - 1, y]?.Data.tileType) ? x - i : x - 1 - i;
                                if (cx >= 0 && cx < width && grid[cx, y] != null)
                                    result.MatchedTiles.Add(grid[cx, y]);
                            }
                            if (matchLength == 4) result.LineOf4.Add(new Vector2Int(x - 2, y));
                            else if (matchLength >= 5) result.LineOf5.Add(new Vector2Int(x - 3, y));
                        }
                        matchLength = 1;
                    }
                }
            }

            // 2. Alignements verticaux
            for (int x = 0; x < width; x++)
            {
                int matchLength = 1;
                for (int y = 0; y < height; y++)
                {
                    bool isEnd = (y == height - 1);
                    if (!isEnd && grid[x, y] != null && grid[x, y + 1] != null &&
                        grid[x, y].Data.tileType == grid[x, y + 1].Data.tileType)
                    {
                        matchLength++;
                    }
                    else
                    {
                        if (matchLength >= 3)
                        {
                            for (int i = 0; i < matchLength; i++)
                            {
                                int cy = isEnd && (grid[x, y] != null && y > 0 && grid[x, y].Data.tileType == grid[x, y - 1]?.Data.tileType) ? y - i : y - 1 - i;
                                if (cy >= 0 && cy < height && grid[x, cy] != null)
                                    result.MatchedTiles.Add(grid[x, cy]);
                            }
                            if (matchLength == 4) result.LineOf4.Add(new Vector2Int(x, y - 2));
                            else if (matchLength >= 5) result.LineOf5.Add(new Vector2Int(x, y - 3));
                        }
                        matchLength = 1;
                    }
                }
            }

            return result;
        }
    }
}
```

### B. Contrôleur de Grille 6x6 (`GridManager.cs`)
```csharp
using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace FarmBloom.Match3
{
    public class GridManager : MonoBehaviour
    {
        public static GridManager Instance { get; private set; }
        public event Action<TileType, int> OnTilesHarvested;
        public event Action OnTurnCompleted;

        [SerializeField] private int width = 6;
        [SerializeField] private int height = 6;
        [SerializeField] private float cellSize = 1.1f;
        [SerializeField] private GameObject tilePrefab;
        [SerializeField] private TileData[] availableTileData;

        private TileController[,] grid;
        public bool IsProcessingTurn { get; private set; }

        private void Awake() => Instance = this;
        private void Start() => InitializeGrid();

        public void InitializeGrid()
        {
            grid = new TileController[width, height];
            Vector2 offset = new Vector2(-(width - 1) * cellSize * 0.5f, -(height - 1) * cellSize * 0.5f);

            for (int x = 0; x < width; x++)
            {
                for (int y = 0; y < height; y++)
                {
                    TileData data = GetValidRandomTileData(x, y);
                    Vector3 pos = new Vector3(offset.x + x * cellSize, offset.y + y * cellSize, 0f);
                    SpawnTile(data, x, y, pos);
                }
            }
        }

        private TileData GetValidRandomTileData(int x, int y)
        {
            List<TileData> candidates = new List<TileData>(availableTileData);
            if (x >= 2 && grid[x - 1, y] != null && grid[x - 2, y] != null && grid[x - 1, y].Data == grid[x - 2, y].Data)
                candidates.Remove(grid[x - 1, y].Data);
            if (y >= 2 && grid[x, y - 1] != null && grid[x, y - 2] != null && grid[x, y - 1].Data == grid[x, y - 2].Data)
                candidates.Remove(grid[x, y - 1].Data);
            return candidates[UnityEngine.Random.Range(0, candidates.Count)];
        }

        private TileController SpawnTile(TileData data, int x, int y, Vector3 pos)
        {
            GameObject obj = Instantiate(tilePrefab, pos, Quaternion.identity, transform);
            TileController tile = obj.GetComponent<TileController>();
            tile.Initialize(data, x, y, this);
            grid[x, y] = tile;
            return tile;
        }

        public void TrySwapTiles(int x1, int y1, int x2, int y2)
        {
            if (IsProcessingTurn || x2 < 0 || x2 >= width || y2 < 0 || y2 >= height) return;
            StartCoroutine(SwapAndProcessTurnRoutine(x1, y1, x2, y2));
        }

        private IEnumerator SwapAndProcessTurnRoutine(int x1, int y1, int x2, int y2)
        {
            IsProcessingTurn = true;
            TileController t1 = grid[x1, y1];
            TileController t2 = grid[x2, y2];

            grid[x1, y1] = t2; grid[x2, y2] = t1;
            t1.SetGridCoordinates(x2, y2); t2.SetGridCoordinates(x1, y1);

            Vector3 p1 = t1.transform.position; Vector3 p2 = t2.transform.position;
            t1.AnimateMoveTo(p2, 0.2f); t2.AnimateMoveTo(p1, 0.2f);
            yield return new WaitForSeconds(0.22f);

            MatchResult match = MatchFinder.FindMatches(grid, width, height);
            if (match.MatchedTiles.Count > 0)
            {
                OnTurnCompleted?.Invoke();
                yield return ProcessMatchesCascadeRoutine();
            }
            else
            {
                grid[x1, y1] = t1; grid[x2, y2] = t2;
                t1.SetGridCoordinates(x1, y1); t2.SetGridCoordinates(x2, y2);
                t1.AnimateMoveTo(p1, 0.15f); t2.AnimateMoveTo(p2, 0.15f);
                yield return new WaitForSeconds(0.18f);
            }
            IsProcessingTurn = false;
        }

        private IEnumerator ProcessMatchesCascadeRoutine()
        {
            while (true)
            {
                MatchResult match = MatchFinder.FindMatches(grid, width, height);
                if (match.MatchedTiles.Count == 0) break;

                Dictionary<TileType, int> counts = new Dictionary<TileType, int>();
                foreach (var tile in match.MatchedTiles)
                {
                    TileType type = tile.Data.tileType;
                    counts[type] = counts.TryGetValue(type, out int c) ? c + 1 : 1;
                    grid[tile.GridX, tile.GridY] = null;
                    tile.AnimateDestroy(null);
                }

                foreach (var kvp in counts) OnTilesHarvested?.Invoke(kvp.Key, kvp.Value);
                yield return new WaitForSeconds(0.18f);
                yield return ApplyGravityRoutine();
                yield return RefillTopRoutine();
            }
        }

        private IEnumerator ApplyGravityRoutine()
        {
            Vector2 offset = new Vector2(-(width - 1) * cellSize * 0.5f, -(height - 1) * cellSize * 0.5f);
            for (int x = 0; x < width; x++)
            {
                for (int y = 0; y < height; y++)
                {
                    if (grid[x, y] == null)
                    {
                        for (int aboveY = y + 1; aboveY < height; aboveY++)
                        {
                            if (grid[x, aboveY] != null)
                            {
                                TileController t = grid[x, aboveY];
                                grid[x, y] = t; grid[x, aboveY] = null;
                                t.SetGridCoordinates(x, y);
                                t.AnimateMoveTo(new Vector3(offset.x + x * cellSize, offset.y + y * cellSize, 0f), 0.15f);
                                break;
                            }
                        }
                    }
                }
            }
            yield return new WaitForSeconds(0.18f);
        }

        private IEnumerator RefillTopRoutine()
        {
            Vector2 offset = new Vector2(-(width - 1) * cellSize * 0.5f, -(height - 1) * cellSize * 0.5f);
            for (int x = 0; x < width; x++)
            {
                for (int y = 0; y < height; y++)
                {
                    if (grid[x, y] == null)
                    {
                        TileData d = availableTileData[UnityEngine.Random.Range(0, availableTileData.Length)];
                        Vector3 spawn = new Vector3(offset.x + x * cellSize, offset.y + (height + 1) * cellSize, 0f);
                        Vector3 target = new Vector3(offset.x + x * cellSize, offset.y + y * cellSize, 0f);
                        TileController t = SpawnTile(d, x, y, spawn);
                        t.AnimateMoveTo(target, 0.2f);
                    }
                }
            }
            yield return new WaitForSeconds(0.22f);
        }
    }
}
```

---

## 4. Système de Parcelles & Minuteur Temps Réel (`FarmPlot.cs`)

Gère la plantation, les phases visuelles de pousse et le calcul en temps réel persistant (`DateTime.UtcNow`).

```csharp
using System;
using UnityEngine;

namespace FarmBloom.Farm
{
    public enum PlotState { Empty, Growing, ReadyToHarvest }

    [RequireComponent(typeof(SpriteRenderer), typeof(Collider2D))]
    public class FarmPlot : MonoBehaviour
    {
        [SerializeField] private Sprite emptyPlotSprite;
        private SpriteRenderer spriteRenderer;
        
        public PlotState State { get; private set; } = PlotState.Empty;
        public CropData CurrentCrop { get; private set; }
        private DateTime plantTimeUtc;

        private void Awake() => spriteRenderer = GetComponent<SpriteRenderer>();

        private void Update()
        {
            if (State != PlotState.Growing || CurrentCrop == null) return;

            double elapsedSeconds = (DateTime.UtcNow - plantTimeUtc).TotalSeconds;
            float progress = Mathf.Clamp01((float)(elapsedSeconds / CurrentCrop.growthDurationSeconds));

            // Mise à jour de l'étape visuelle
            int stageCount = CurrentCrop.growthStageSprites.Length;
            if (stageCount > 0)
            {
                int currentStageIndex = Mathf.Min((int)(progress * stageCount), stageCount - 1);
                spriteRenderer.sprite = CurrentCrop.growthStageSprites[currentStageIndex];
            }

            if (progress >= 1f)
            {
                State = PlotState.ReadyToHarvest;
            }
        }

        public bool Plant(CropData crop)
        {
            if (State != PlotState.Empty || crop == null) return false;

            CurrentCrop = crop;
            plantTimeUtc = DateTime.UtcNow;
            State = PlotState.Growing;
            return true;
        }

        public bool Harvest(out CropData harvestedCrop)
        {
            if (State != PlotState.ReadyToHarvest)
            {
                harvestedCrop = null;
                return false;
            }

            harvestedCrop = CurrentCrop;
            CurrentCrop = null;
            State = PlotState.Empty;
            spriteRenderer.sprite = emptyPlotSprite;
            return true;
        }

        private void OnMouseDown()
        {
            if (State == PlotState.ReadyToHarvest && Harvest(out CropData crop))
            {
                // Donner les récompenses au joueur
                FarmBloom.Core.ResourceManager.Instance?.AddResource("coins", crop.coinsReward);
            }
        }
    }
}
```

---

## 5. Système d'Amélioration de la Grange (`BarnController.cs`)

Vérifie les ressources requises (bois, marteaux, pièces) et met à jour le niveau et la capacité de stockage.

```csharp
using System;
using UnityEngine;

namespace FarmBloom.Buildings
{
    public class BarnController : MonoBehaviour
    {
        [Header("Configuration")]
        [SerializeField] private BuildingUpgradeData[] levelUpgrades; // Index 0 = N2, Index 1 = N3...
        [SerializeField] private SpriteRenderer barnRenderer;

        public int CurrentLevel { get; private set; } = 1;
        public int CurrentStorageCapacity { get; private set; } = 50;

        public event Action<int, int> OnBarnUpgraded; // (NouveauNiveau, NouvelleCapacité)

        public BuildingUpgradeData GetNextUpgradeData()
        {
            int nextIndex = CurrentLevel - 1;
            return (nextIndex >= 0 && nextIndex < levelUpgrades.Length) ? levelUpgrades[nextIndex] : null;
        }

        public bool CanUpgrade()
        {
            BuildingUpgradeData next = GetNextUpgradeData();
            if (next == null) return false;

            var res = FarmBloom.Core.ResourceManager.Instance;
            if (res == null) return false;

            foreach (var req in next.requirements)
            {
                if (!res.HasEnough(req.resourceId, req.amountRequired))
                    return false;
            }

            return true;
        }

        public bool TryUpgrade()
        {
            if (!CanUpgrade()) return false;

            BuildingUpgradeData next = GetNextUpgradeData();
            var res = FarmBloom.Core.ResourceManager.Instance;

            // Déduire les ressources
            foreach (var req in next.requirements)
            {
                res.ConsumeResource(req.resourceId, req.amountRequired);
            }

            // Appliquer l'amélioration
            CurrentLevel = next.targetLevel;
            CurrentStorageCapacity = next.newStorageCapacity;
            if (barnRenderer != null && next.upgradedSprite != null)
            {
                barnRenderer.sprite = next.upgradedSprite;
            }

            OnBarnUpgraded?.Invoke(CurrentLevel, CurrentStorageCapacity);
            return true;
        }
    }
}
```
