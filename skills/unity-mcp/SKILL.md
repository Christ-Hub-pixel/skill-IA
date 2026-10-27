---
name: unity-mcp
description: Unity game development, C# scripting, and editor automation using CoplayDev/unity-mcp. Use when the user asks about Unity, game development in Unity, C# Unity scripts, controlling Unity Editor via MCP, GameObject creation, scene hierarchy, physics, prefabs, or Unity Package Manager.
metadata:
  origin: custom
---

# Unity & Unity-MCP Development Guide

Guide for building Unity projects, writing idiomatic C# scripts for Unity, and integrating **CoplayDev/unity-mcp** for AI-driven editor automation.

---

## 1. When to Activate

- Writing, reviewing, or debugging Unity C# scripts (`MonoBehaviour`, `ScriptableObject`).
- Automating Unity Editor operations (creating GameObjects, adding components, building scenes).
- Setting up or troubleshooting the **CoplayDev/unity-mcp** integration.
- Fixing Unity compilation errors, console warnings, or physics/lifecycle bugs.
- Structuring Unity project architecture (input systems, state management, event buses).

---

## 2. CoplayDev/unity-mcp Quick Reference

### Package Installation in Unity
In Unity (`2021.3 LTS` to `6.x`):
- **Window > Package Manager > `+` > Add package from git URL...**
- URL: `https://github.com/CoplayDev/unity-mcp.git?path=/MCPForUnity#main`
- Alternative (OpenUPM): `openupm add com.coplaydev.unity-mcp`

### Automatic Configuration
- **Window > MCP for Unity > Configure All Detected Clients**

### Manual MCP Server Configuration
```json
{
  "mcpServers": {
    "coplay-mcp": {
      "command": "uvx",
      "args": [
        "--python",
        ">=3.11",
        "coplay-mcp-server@latest"
      ],
      "env": {
        "MCP_TOOL_TIMEOUT": "720000"
      }
    }
  }
}
```

### Available Capabilities via MCP
- **Scene Management:** Create, duplicate, delete, and inspect GameObjects and transform hierarchies.
- **Component Management:** Add components (`Rigidbody`, `Collider`, custom scripts), modify properties and serialized fields.
- **Console Monitoring:** Read compiler errors and runtime exceptions directly from the Unity console.
- **Testing:** Run PlayMode and EditMode tests through Unity Test Framework.

---

## 3. Unity C# Scripting Standards

### Component Lifecycle & Performance Rules
1. **Caching References:** Cache `GetComponent<T>()` in `Awake()` or `Start()`. Never call `GetComponent` inside `Update()` or `FixedUpdate()`.
2. **Physics in FixedUpdate:** All `Rigidbody` forces, velocities, and physics operations MUST live in `FixedUpdate()`, never `Update()`.
3. **Delta Time:** Multiply movement and timers by `Time.deltaTime` in `Update()`, or `Time.fixedDeltaTime` in `FixedUpdate()`.
4. **Avoid Empty Lifecycle Methods:** Remove empty `Update()`, `Start()`, or `Awake()` methods.
5. **Garbage Collection (GC) Hygiene:** Avoid allocating objects, arrays, or string concatenations in update loops. Use `StringBuilder` or object pooling.

### Serialization & Inspector
- Use `[SerializeField] private` instead of `public` fields to expose variables in the Inspector while preserving encapsulation.
- Use `[RequireComponent(typeof(T))]` when a script depends on another component (e.g. `Rigidbody`, `AudioSource`).
- Use `[Header("...")]` and `[Tooltip("...")]` to document inspector parameters.

---

## 4. Architecture Patterns in Unity

- **ScriptableObjects:** Use for shared game data (enemy stats, item databases) and decoupled event channels.
- **Object Pooling:** Use for spawned entities (bullets, particles, enemies) to prevent GC allocation spikes.
- **State Machine:** Use for character behaviors, AI states, and game flow.
