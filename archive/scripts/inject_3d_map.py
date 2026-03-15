import re

html_path = "vehicle_lab_vanilla/cie_pro.html"
with open(html_path, "r") as f:
    content = f.read()

# 1. Add Plotly.js to the <head>
if 'plotly-latest.min.js' not in content:
    content = content.replace(
        '</head>',
        '    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>\n</head>'
    )

# 2. Replace the static image div with a Plotly container
old_html = """<div class="lg:col-span-8 bg-black rounded-[2rem] border border-slate-800 overflow-hidden relative min-h-[300px]">
                        <img src="https://images.unsplash.com/photo-1551288049-bbbda536ad3a?auto=format&fit=crop&q=80&w=1200"
                            class="w-full h-full object-cover opacity-40 mix-blend-screen" alt="Heatmap" />
                        <div class="absolute bottom-8 left-8 flex gap-4">
                            <div class="px-4 py-2 bg-black/80 border border-white/10 rounded-xl text-[10px] font-mono">Z: Torque (Nm)
                            </div>
                            <div class="px-4 py-2 bg-black/80 border border-white/10 rounded-xl text-[10px] font-mono">X: Speed (RPM)
                            </div>
                        </div>
                    </div>"""

new_html = """<div class="lg:col-span-8 bg-black rounded-[2rem] border border-slate-800 overflow-hidden relative min-h-[400px]" id="plotly-surface-container">
                        <!-- Plotly will render here -->
                    </div>"""

content = content.replace(old_html, new_html)

# 3. Add the script to generate the 3D surface
script_to_add = """
    <!-- Plotly 3D Surface Map Script -->
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Generate some realistic-looking engine map data
            const z_data = [];
            const x_rpm = [];
            const y_load = [];
            
            for (let i = 0; i < 20; i++) {
                x_rpm.push(1000 + i * 300); // 1000 to 6700 RPM
                y_load.push(10 + i * 4.5);  // 10 to 100% Load
            }
            
            for (let i = 0; i < 20; i++) {
                let row = [];
                for (let j = 0; j < 20; j++) {
                    // Create a curved surface representing volumetric efficiency / torque
                    let x = x_rpm[j] / 7000;
                    let y = y_load[i] / 100;
                    let z = (Math.sin(x * Math.PI) * Math.sin(y * Math.PI)) * 400 + (y*100) + (x*50);
                    row.push(z);
                }
                z_data.push(row);
            }

            const data = [{
                z: z_data,
                x: x_rpm,
                y: y_load,
                type: 'surface',
                colorscale: 'Portland', // A good fiery heat engineering color
                showscale: false,
                contours: {
                    z: {
                        show: true,
                        usecolormap: true,
                        highlightcolor: "#42f462",
                        project: {z: true}
                    }
                }
            }];

            const layout = {
                paper_bgcolor: 'rgba(0,0,0,0)',
                plot_bgcolor: 'rgba(0,0,0,0)',
                margin: { l: 0, r: 0, b: 0, t: 0 },
                scene: {
                    xaxis: { title: 'Speed (RPM)', color: '#94a3b8', gridcolor: '#334155' },
                    yaxis: { title: 'Load (%)', color: '#94a3b8', gridcolor: '#334155' },
                    zaxis: { title: 'Torque (Nm)', color: '#94a3b8', gridcolor: '#334155' },
                    camera: {
                        eye: {x: -1.5, y: -1.5, z: 1.2}
                    }
                }
            };

            const config = {responsive: true, displayModeBar: false};

            Plotly.newPlot('plotly-surface-container', data, layout, config);
        });
    </script>
</body>
"""

content = content.replace("</body>", script_to_add)

with open(html_path, "w") as f:
    f.write(content)

print("Injected Plotly 3D map.")
