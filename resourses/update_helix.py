import re

with open('vehicle_lab_vanilla/helix.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update The Data Pipeline
data_old = """                            <div class="flex gap-4">
                                <div class="h-10 w-10 rounded bg-primary/20 flex items-center justify-center shrink-0">
                                    <span class="material-symbols-outlined text-primary neon-glow">swap_horiz</span>
                                </div>
                                <div>
                                    <h4 class="text-lg font-bold">DCM Import/Export</h4>
                                    <p class="text-slate-400">Industry-standard data exchange formats supported with
                                        full round-trip integrity checks.</p>
                                </div>
                            </div>
                            <div class="flex gap-4">
                                <div class="h-10 w-10 rounded bg-primary/20 flex items-center justify-center shrink-0">
                                    <span class="material-symbols-outlined text-primary neon-glow">memory</span>
                                </div>
                                <div>
                                    <h4 class="text-lg font-bold">Hex Generation</h4>
                                    <p class="text-slate-400">Compile your calibrations into high-fidelity Intel Hex or
                                        S19 Motorola formats with one click.</p>
                                </div>
                            </div>"""

data_new = """                            <div class="flex gap-4">
                                <div class="h-10 w-10 rounded bg-primary/20 flex items-center justify-center shrink-0">
                                    <span class="material-symbols-outlined text-primary neon-glow">account_tree</span>
                                </div>
                                <div>
                                    <h4 class="text-lg font-bold">vCDM-Compliant Workflow</h4>
                                    <p class="text-slate-400">Production-ready database schema powered by SQLAlchemy handling full variant tree logic and Role-Based Access Control (RBAC).</p>
                                </div>
                            </div>
                            <div class="flex gap-4">
                                <div class="h-10 w-10 rounded bg-primary/20 flex items-center justify-center shrink-0">
                                    <span class="material-symbols-outlined text-primary neon-glow">memory</span>
                                </div>
                                <div>
                                    <h4 class="text-lg font-bold">Hex Generation</h4>
                                    <p class="text-slate-400">Compile calibrations into high-fidelity Intel Hex or S19 formats dynamically through our real-time generation pipeline.</p>
                                </div>
                            </div>"""
html = html.replace(data_old, data_new)

# 2. Update Enterprise Collaboration Headers
collab_old = """                        <h3 class="text-4xl font-bold mb-6">Built for Distributed Engineering Teams</h3>"""
collab_new = """                        <h3 class="text-4xl font-bold mb-4">From Desktop Silos to Cloud Collaboration</h3>
                        <p class="text-slate-400 mb-8 max-w-xl">Escape the legacy trap of heavy Windows clients and hardware dongles. Shift to zero-install, native browser access powered by Next.js, React, and WebSockets.</p>"""
html = html.replace(collab_old, collab_new)


# 3. Insert The Hierarchy of Truth before QA Section
hierarchy = """
        <!-- The Hierarchy of Truth -->
        <section class="py-24" id="hierarchy">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center mb-16">
                    <h2 class="text-primary font-bold tracking-widest uppercase text-sm mb-4">Variant Management</h2>
                    <h3 class="text-4xl font-bold mb-4">The Hierarchy of Truth: Structuring the Chaos</h3>
                    <p class="text-slate-400 max-w-2xl mx-auto">Multi-tenant management from OEM down to individual variant. HELIX introduces 'OEM' as a first-class entity with a Single Command Center to view all projects across vehicle programs.</p>
                </div>
                <div class="max-w-4xl mx-auto bg-slate-900 border border-slate-800 rounded-3xl p-10 font-mono text-xs text-slate-400 relative overflow-hidden shadow-2xl">
                     <ul class="space-y-4 relative z-10">
                        <li>
                            <div class="flex items-center gap-3 text-white text-sm bg-slate-800/50 p-3 rounded-lg border border-slate-700 w-64 mx-auto shadow">
                                <span class="material-symbols-outlined text-primary">domain</span>
                                <strong class="uppercase font-sans tracking-widest text-[11px]">OEM / Honda</strong>
                            </div>
                            <ul class="pl-32 mt-4 space-y-4 border-l-2 border-slate-800 ml-32 border-b-2 rounded-bl-xl pb-4">
                                <li class="relative">
                                    <div class="absolute -left-32 top-4 w-32 border-t-2 border-slate-800"></div>
                                    <div class="flex items-center gap-3 text-slate-200 bg-slate-800/30 p-3 rounded-lg border border-slate-700/50 w-64 shadow">
                                        <span class="material-symbols-outlined text-neon-purple text-sm">view_timeline</span>
                                        <strong>Program: EV Platform 2026</strong>
                                    </div>
                                    <ul class="pl-8 mt-4 space-y-4 border-l-2 border-slate-800/50 ml-4">
                                         <li class="relative">
                                            <div class="absolute -left-8 top-4 w-8 border-t-2 border-slate-800/50"></div>
                                            <div class="flex items-center gap-3 text-slate-300 bg-slate-800/20 p-2 rounded-lg border border-slate-700/30 w-56">
                                                <span class="material-symbols-outlined text-blue-400 text-sm">folder</span>
                                                Project: Model S City
                                            </div>
                                            <ul class="pl-8 mt-2 space-y-2 border-l border-slate-800/30 ml-4 pb-2">
                                                <li class="relative flex items-center gap-2">
                                                     <div class="absolute -left-8 top-3 w-8 border-t border-slate-800/30"></div>
                                                     <div class="bg-black/40 px-3 py-1.5 rounded border border-slate-800/50 w-48 text-slate-400">Variant: Eco Mode</div>
                                                </li>
                                                <li class="relative flex items-center gap-2">
                                                     <div class="absolute -left-8 top-3 w-8 border-t border-slate-800/30"></div>
                                                     <div class="bg-black/40 px-3 py-1.5 rounded border border-slate-800/50 w-48 text-slate-400">Variant: Standard</div>
                                                </li>
                                            </ul>
                                         </li>
                                    </ul>
                                </li>
                                <li class="relative">
                                    <div class="absolute -left-32 top-4 w-32 border-t-2 border-slate-800"></div>
                                    <div class="flex items-center gap-3 text-slate-200 bg-slate-800/30 p-3 rounded-lg border border-slate-700/50 w-64">
                                        <span class="material-symbols-outlined text-neon-purple text-sm">view_timeline</span>
                                        <strong>Program: Legacy ICE</strong>
                                    </div>
                                </li>
                            </ul>
                        </li>
                     </ul>
                     <div class="absolute bottom-0 right-0 w-96 h-96 bg-primary/10 blur-[100px] -z-0"></div>
                </div>
            </div>
        </section>
"""

html = html.replace('        <!-- Zero-Defect Calibration / QA -->', hierarchy + '        <!-- Zero-Defect Calibration / QA -->')

with open('vehicle_lab_vanilla/helix.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated helix.html")
