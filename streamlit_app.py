import streamlit as st
import pandas as pd
import itertools

def calculate_weighted_totals(alternatives, weighted_scores):
    total_scores = {}
    details = {}
    for alt in alternatives:
        scores = weighted_scores[alt]
        total = sum(scores)
        detail = " + ".join([f"({score:.1f})" for score in scores])
        details[alt] = (detail, total)
        total_scores[alt] = total
    return total_scores, details

def calculate_copeland_score(total_scores):
    alternatives = list(total_scores.keys())
    copeland_scores = {alt: 0 for alt in alternatives}

    for alt1, alt2 in itertools.combinations(alternatives, 2):
        if total_scores[alt1] > total_scores[alt2]:
            copeland_scores[alt1] += 1
            copeland_scores[alt2] -= 1
        elif total_scores[alt1] < total_scores[alt2]:
            copeland_scores[alt2] += 1
            copeland_scores[alt1] -= 1
        # draw = no change
    return copeland_scores

def main():
    st.set_page_config(page_title="Copeland Score Calculator", layout="wide")
    st.title("🔢 Copeland Score Calculator")

    # Step 1: Kriteria dan Bobot - dengan data editor
    st.header("1. Kriteria dan Bobot")
    st.markdown("Edit nama kriteria dan bobotnya (total bobot harus 100%)")

    default_data = pd.DataFrame({
        "Kriteria": ["Harga", "Kualitas", "Daya Tahan", "Layanan"],
        "Bobot (%)": [25, 25, 25, 25]
    })

    criteria_df = st.data_editor(
        default_data,
        num_rows="dynamic",
        use_container_width=True,
        key="kriteria_bobot"
    )

    # Validasi
    if criteria_df.empty or "Kriteria" not in criteria_df.columns or "Bobot (%)" not in criteria_df.columns:
        st.error("Harap masukkan minimal satu kriteria dengan bobot.")
        return

    criteria_df.dropna(inplace=True)
    criteria_df["Kriteria"] = criteria_df["Kriteria"].astype(str).str.strip()
    criteria_df["Bobot (%)"] = pd.to_numeric(criteria_df["Bobot (%)"], errors="coerce").fillna(0).astype(int)

    criteria = criteria_df["Kriteria"].tolist()
    weights = dict(zip(criteria_df["Kriteria"], criteria_df["Bobot (%)"]))
    total_weight = sum(weights.values())

    st.progress(min(total_weight, 100) / 100.0)
    if total_weight != 100:
        st.warning("⚠️ Total bobot saat ini adalah {}%. Harus tepat 100%.".format(total_weight))
        return

    # Step 2: Alternatif
    st.header("2. Alternatif")
    alternatives = st.text_area("Masukkan nama alternatif (satu per baris):", "Vendor A\nVendor B\nVendor C").split("\n")
    alternatives = [alt.strip() for alt in alternatives if alt.strip()]
    
    if len(alternatives) < 2:
        st.error("Masukkan minimal dua alternatif.")
        return

    # Step 3: Nilai
    st.header("3. Nilai Alternatif terhadap Kriteria")
    weighted_scores = {alt: [] for alt in alternatives}
    raw_scores = {alt: {} for alt in alternatives}

    for alt in alternatives:
        with st.expander(f"Nilai untuk {alt}", expanded=True):
            for criterion in criteria:
                score = st.number_input(
                    f"{criterion} - {alt}",
                    min_value=0, max_value=100, value=70, step=1,
                    key=f"{alt}_{criterion}"
                )
                weighted = score * (weights[criterion] / 100)
                weighted_scores[alt].append(weighted)
                raw_scores[alt][criterion] = score

    # Step 4: Hitung
    if st.button("📊 Hitung Skor Copeland"):
        st.header("📈 Hasil Perhitungan")

        total_scores, details = calculate_weighted_totals(alternatives, weighted_scores)
        copeland_scores = calculate_copeland_score(total_scores)

        # Rincian perhitungan
        st.subheader("🔍 Rincian Skor Total")
        for alt in alternatives:
            formula_parts = [f"{raw_scores[alt][c]}×{weights[c]/100:.2f}" for c in criteria]
            formula = " + ".join(formula_parts)
            st.write(f"**{alt}** = {formula} = **{total_scores[alt]:.2f}**")

        # Hasil akhir
        result_df = pd.DataFrame({
            "Alternatif": alternatives,
            "Total Skor": [total_scores[alt] for alt in alternatives],
            "Skor Copeland": [copeland_scores[alt] for alt in alternatives]
        }).sort_values(by="Skor Copeland", ascending=False).reset_index(drop=True)

        # Peringkat + Medali
        medals = ["🥇", "🥈", "🥉"]
        result_df["Peringkat"] = [medals[i] if i < len(medals) else f"Ke-{i+1}" for i in range(len(result_df))]

        st.subheader("🏆 Hasil Akhir")
        st.dataframe(result_df, use_container_width=True)

        # Pemenang
        winner = result_df.iloc[0]
        st.success(f"✅ **{winner['Alternatif']}** adalah yang terbaik berdasarkan Copeland Score ({winner['Skor Copeland']})!")

if __name__ == "__main__":
    main()
