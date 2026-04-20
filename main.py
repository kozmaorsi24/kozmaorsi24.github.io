import pandas as pd
import plotly.express as px

# Excel betöltése
df = pd.read_excel("data.xlsx")

# ===== 1. Scatter (internet vs DFI) =====
fig1 = px.scatter(
    df,
    x="INTERNET",
    y="DFI_FDI",
    color="Orszag",
    title="Internet usage vs Financial Inclusion"
)
fig1.write_html("fig1_scatter.html")

# ===== 2. Idősoros (DFI trend) =====
fig2 = px.line(
    df,
    x="Ev",
    y="DFI_FDI",
    color="Orszag",
    title="DFI over time"
)
fig2.write_html("fig2_line.html")

# ===== 3. Bar chart (átlag DFI országonként) =====
avg_dfi = df.groupby("Orszag")["DFI_FDI"].mean().reset_index()

fig3 = px.bar(
    avg_dfi,
    x="Orszag",
    y="DFI_FDI",
    title="Average Financial Inclusion by Country"
)
fig3.write_html("fig3_bar.html")

# ===== 4. Bubble chart =====
fig4 = px.scatter(
    df,
    x="INTERNET",
    y="DFI_FDI",
    size="E_COMM",
    color="Orszag",
    title="Digitalization factors and DFI"
)
fig4.write_html("fig4_bubble.html")

# ===== 5. Heatmap =====
pivot = df.pivot(index="Orszag", columns="Ev", values="DFI_FDI")

fig5 = px.imshow(
    pivot,
    title="DFI Heatmap (Country vs Year)"
)
fig5.write_html("fig5_heatmap.html")

# ===== 6. Human capital vs DFI =====
fig6 = px.scatter(
    df,
    x="HC",
    y="DFI_FDI",
    color="Orszag",
    title="Human Capital vs Financial Inclusion"
)
fig6.write_html("fig6_humancap.html")

print("Minden ábra elkészült!")