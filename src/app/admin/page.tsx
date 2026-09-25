"use client";
import { useEffect, useState } from "react";
import { Plus, Trash2, Pencil, RefreshCw, LayoutDashboard, Package, FolderOpen, Video, Clapperboard, Briefcase, MapPin, Newspaper, Inbox, Settings2 } from "lucide-react";

const RESOURCES = [
  { key: "products", label: "Products", icon: Package },
  { key: "product_categories", label: "Product Categories", icon: FolderOpen },
  { key: "videos", label: "Videos", icon: Video },
  { key: "video_categories", label: "Video Categories", icon: Clapperboard },
  { key: "projects", label: "Projects", icon: Briefcase },
  { key: "locations", label: "Locations", icon: MapPin },
  { key: "posts", label: "Blog Posts", icon: Newspaper },
  { key: "inquiries", label: "Inquiries", icon: Inbox },
  { key: "settings", label: "Settings", icon: Settings2 },
];

const HIDE = new Set(["createdAt", "updatedAt"]);

export default function AdminPage() {
  const [res, setRes] = useState("products");
  const [rows, setRows] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);
  const [editing, setEditing] = useState<any | null>(null);
  const [isNew, setIsNew] = useState(false);
  const [msg, setMsg] = useState("");

  async function load(r = res) {
    setLoading(true);
    try {
      const j = await (await fetch(`/api/admin/${r}`)).json();
      setRows(j.rows || []);
    } catch { setRows([]); }
    setLoading(false);
  }

  useEffect(() => { load(res); }, [res]);

  async function save() {
    if (!editing) return;
    setMsg("Saving…");
    const payload: any = { ...editing };
    for (const k of ["gallery", "features", "specifications", "relatedIds", "relatedProducts", "relatedProjects", "relatedLocations", "tags"]) {
      if (typeof payload[k] === "string") {
        try { payload[k] = JSON.parse(payload[k]); }
        catch {
          if (k === "specifications") payload[k] = payload[k].split("\n").filter(Boolean).map((l: string) => { const [label, ...rest] = l.split(":"); return { label: label.trim(), value: rest.join(":").trim() }; });
          else if (k === "relatedIds" || k.startsWith("related")) payload[k] = payload[k].split(",").map((x: string) => Number(x.trim())).filter(Boolean);
          else payload[k] = payload[k].split("\n").map((x: string) => x.trim()).filter(Boolean);
        }
      }
    }
    for (const k of ["categoryId", "displayOrder", "sortOrder", "productId"]) {
      if (payload[k] === "" || payload[k] === null) payload[k] = null;
      else if (payload[k] !== undefined) payload[k] = Number(payload[k]);
    }
    try {
      const url = isNew ? `/api/admin/${res}` : `/api/admin/${res}/${editing.id}`;
      const r = await fetch(url, { method: isNew ? "POST" : "PUT", headers: { "Content-Type": "application/json" }, body: JSON.stringify(payload) });
      const j = await r.json();
      setMsg(j.ok ? "Saved ✓" : "Error: " + j.error);
      if (j.ok) { setEditing(null); load(); }
    } catch (e: any) { setMsg("Error: " + e.message); }
  }

  async function remove(id: number) {
    if (!confirm("Delete this record?")) return;
    await fetch(`/api/admin/${res}/${id}`, { method: "DELETE" });
    load();
  }

  const fields = editing ? Object.keys(editing).filter((k) => !HIDE.has(k) && k !== "id") : [];

  function fieldInput(k: string, v: any) {
    if (typeof v === "boolean") {
      return (
        <button type="button" onClick={() => setEditing({ ...editing, [k]: !v })} className={`rounded-xl px-4 py-2.5 text-sm font-bold ${v ? "bg-emerald-600 text-white" : "bg-stone-200"}`}>
          {v ? "Yes / On" : "No / Off"}
        </button>
      );
    }
    if (v !== null && typeof v === "object") {
      return <textarea value={JSON.stringify(v, null, 1)} rows={3} onChange={(e) => setEditing({ ...editing, [k]: e.target.value })} className="w-full rounded-xl border px-3 py-2 font-mono text-xs" />;
    }
    if (typeof v === "string" && (v.length > 120 || k.toLowerCase().includes("description") || k.toLowerCase().includes("content") || k.toLowerCase().includes("message"))) {
      return <textarea value={v || ""} rows={3} onChange={(e) => setEditing({ ...editing, [k]: e.target.value })} className="w-full rounded-xl border px-3 py-2 text-sm" />;
    }
    return <input value={v ?? ""} onChange={(e) => setEditing({ ...editing, [k]: e.target.value })} className="w-full rounded-xl border px-3 py-2 text-sm" />;
  }

  return (
    <div className="bg-[#f4f1ec]">
      <section className="bg-[#141210] py-10 text-white">
        <div className="bp-container flex flex-wrap items-center justify-between gap-4">
          <div>
            <p className="flex items-center gap-2 text-xs font-black uppercase tracking-[0.22em] text-orange-400"><LayoutDashboard className="h-4 w-4" /> BrickPoint Admin</p>
            <h1 className="font-display mt-1 text-3xl font-black">Content Manager</h1>
            <p className="mt-1 text-sm text-white/60">Manage products, categories, videos, projects, locations, posts, inquiries & settings — no code needed.</p>
          </div>
          <div className="flex gap-2">
            <button onClick={() => load()} className="inline-flex items-center gap-2 rounded-xl bg-white/10 px-4 py-2.5 text-sm font-bold hover:bg-white/15"><RefreshCw className="h-4 w-4" /> Reload</button>
            <a href="/api/seed" target="_blank" rel="noopener" className="btn-brick inline-flex items-center gap-2 rounded-xl px-4 py-2.5 text-sm font-bold text-white">Re-seed Demo</a>
          </div>
        </div>
      </section>
      <div className="bp-container flex gap-6 py-8">
        <aside className="hidden w-60 shrink-0 lg:block">
          <div className="sticky top-24 space-y-1 rounded-2xl border bg-white p-2">
            {RESOURCES.map((r) => (
              <button key={r.key} onClick={() => { setRes(r.key); setEditing(null); }} className={`flex w-full items-center gap-2.5 rounded-xl px-4 py-2.5 text-sm font-semibold ${res === r.key ? "bg-[#141210] text-white" : "hover:bg-stone-100"}`}>
                <r.icon className="h-4 w-4" /> {r.label}
              </button>
            ))}
          </div>
        </aside>
        <div className="min-w-0 flex-1">
          <div className="mb-4 flex gap-2 overflow-x-auto no-scrollbar lg:hidden">
            {RESOURCES.map((r) => (
              <button key={r.key} onClick={() => { setRes(r.key); setEditing(null); }} className={`shrink-0 rounded-full px-4 py-2 text-xs font-bold ${res === r.key ? "bg-[#141210] text-white" : "border bg-white"}`}>{r.label}</button>
            ))}
          </div>
          <div className="flex items-center justify-between">
            <h2 className="font-display text-xl font-black">{RESOURCES.find((r) => r.key === res)?.label} <span className="text-sm font-semibold text-stone-500">({rows.length})</span></h2>
            {res !== "inquiries" && (
              <button onClick={() => { const base: any = rows[0] ? { ...rows[0] } : { name: "", slug: "" }; delete base.id; Object.keys(base).forEach((k) => { base[k] = typeof base[k] === "boolean" ? false : typeof base[k] === "number" ? 0 : Array.isArray(base[k]) ? [] : ""; }); setEditing(base); setIsNew(true); setMsg(""); }} className="btn-brick inline-flex items-center gap-2 rounded-xl px-4 py-2.5 text-sm font-bold text-white">
                <Plus className="h-4 w-4" /> Add New
              </button>
            )}
          </div>
          {msg && <p className="mt-2 text-sm font-semibold text-orange-700">{msg}</p>}
          {editing && (
            <div className="mt-4 rounded-2xl border-2 border-orange-200 bg-white p-5">
              <h3 className="font-display font-black">{isNew ? "Add" : "Edit"} — {res}</h3>
              <p className="mt-1 text-xs text-stone-500">Arrays (gallery, features, tags): one item per line or valid JSON. Specifications: one per line as “Label: Value”. Related IDs: comma-separated.</p>
              <div className="mt-4 grid gap-4 md:grid-cols-2">
                {fields.map((k) => (
                  <div key={k} className={k.toLowerCase().includes("description") || k.toLowerCase().includes("content") ? "md:col-span-2" : ""}>
                    <label className="mb-1 block text-xs font-black uppercase tracking-wider text-stone-500">{k}</label>
                    {fieldInput(k, editing[k])}
                  </div>
                ))}
              </div>
              <div className="mt-4 flex gap-2">
                <button onClick={save} className="btn-brick rounded-xl px-6 py-2.5 text-sm font-bold text-white">Save</button>
                <button onClick={() => setEditing(null)} className="rounded-xl border px-6 py-2.5 text-sm font-bold">Cancel</button>
              </div>
            </div>
          )}
          <div className="mt-4 overflow-x-auto rounded-2xl border bg-white">
            {loading ? <p className="p-8 text-center text-sm text-stone-500">Loading…</p> : (
              <table className="w-full min-w-[640px] text-left text-sm">
                <thead>
                  <tr className="border-b bg-stone-50 text-xs uppercase tracking-wider text-stone-500">
                    <th className="px-4 py-3">ID</th>
                    <th className="px-4 py-3">Title / Name</th>
                    <th className="px-4 py-3">Slug / Detail</th>
                    <th className="px-4 py-3">Status</th>
                    <th className="px-4 py-3 text-right">Actions</th>
                  </tr>
                </thead>
                <tbody>
                  {rows.map((r: any) => (
                    <tr key={r.id || r.key} className="border-b last:border-0 hover:bg-stone-50">
                      <td className="px-4 py-3 font-mono text-xs">{r.id ?? r.key}</td>
                      <td className="max-w-[240px] truncate px-4 py-3 font-semibold">{r.name || r.title || r.key}</td>
                      <td className="max-w-[220px] truncate px-4 py-3 font-mono text-xs text-stone-500">{r.slug || r.phone || r.value?.slice?.(0, 40) || r.email || ""}</td>
                      <td className="px-4 py-3 text-xs">
                        {r.featured ? <span className="rounded-full bg-amber-100 px-2 py-0.5 font-bold text-amber-800">Featured</span> : r.availability ? <span className="rounded-full bg-emerald-100 px-2 py-0.5 font-bold text-emerald-800">{r.availability}</span> : <span className="text-stone-400">—</span>}
                      </td>
                      <td className="px-4 py-3">
                        <div className="flex justify-end gap-2">
                          <button onClick={() => { setEditing({ ...r }); setIsNew(false); setMsg(""); window.scrollTo({ top: 0, behavior: "smooth" }); }} className="grid h-9 w-9 place-items-center rounded-lg bg-stone-100 hover:bg-stone-200" aria-label="Edit"><Pencil className="h-4 w-4" /></button>
                          {res !== "settings" && <button onClick={() => remove(r.id)} className="grid h-9 w-9 place-items-center rounded-lg bg-red-50 text-red-600 hover:bg-red-100" aria-label="Delete"><Trash2 className="h-4 w-4" /></button>}
                        </div>
                      </td>
                    </tr>
                  ))}
                  {!rows.length && <tr><td colSpan={5} className="p-8 text-center text-stone-500">No records. Click “Add New” or “Re-seed Demo”.</td></tr>}
                </tbody>
              </table>
            )}
          </div>
          <div className="mt-6 rounded-2xl border bg-amber-50 p-5 text-xs leading-relaxed text-amber-900">
            <strong>Admin guide:</strong> Products need <em>name, slug, categoryId</em> (see Product Categories IDs), <em>featuredImage</em> URL, price, unit. Videos need <em>title, slug, categoryId</em> (see Video Categories), <em>videoUrl</em> + <em>sourceType</em> (mp4/youtube/vimeo). Locations need <em>name, slug, mapsUrl</em>. Changes appear on the site instantly.
          </div>
        </div>
      </div>
    </div>
  );
}
