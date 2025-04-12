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
        # draw = no score change

    return copeland_scores

def main():
    st.title("Copeland Score Calculator with Details")
    
    # Input criteria and weights
    st.subheader("1. Kriteria dan Bobot (%)")
    criteria_input = st.text_area("Masukkan kriteria (satu per baris)", "Harga\nKualitas\nDaya Tahan\nLayanan")
    criteria = [c.strip() for c in criteria_input.split("\n") if c.strip()]
    
    weights = {}
    for criterion in criteria:
        weights[criterion] = st.number_input(f"Bobot untuk {criterion} (%)", min_value=0, max_value=100, value=25, step=1)
    
    total_weight = sum(weights.values())
    if total_weight != 100:
        st.warning("Total bobot harus 100%.")
        return
    
    # Input alternatives
    st.subheader("2. Alternatif")
    alternatives = st.text_area("Masukkan nama alternatif (satu per baris)", "Vendor A\nVendor B\nVendor C").split("\n")
    alternatives = [alt.strip() for alt in alternatives if alt.strip()]
    
    if len(alternatives) < 2:
        st.warning("Masukkan minimal dua alternatif.")
        return
    
    # Input scores
    st.subheader("3. Nilai Alternatif terhadap Kriteria")
    weighted_scores = {alt: [] for alt in alternatives}
    raw_scores = {alt: {} for alt in alternatives}

    for alt in alternatives:
        for criterion in criteria:
            score = st.number_input(
                f"Nilai {alt} pada {criterion}", min_value=0, max_value=100, value=70, step=1, key=f"{alt}_{criterion}"
            )
            weighted = score * (weights[criterion] / 100)
            weighted_scores[alt].append(weighted)
            raw_scores[alt][criterion] = score

    if st.button("Hitung Skor Copeland"):
        total_scores, details = calculate_weighted_totals(alternatives, weighted_scores)
        copeland_scores = calculate_copeland_score(total_scores)

        # Tampilkan perhitungan
        st.markdown("**Hasil:**")
        st.code("Perhitungan:")
        for alt in alternatives:
            formula_parts = [f"{raw_scores[alt][c]}×{weights[c]/100:.1f}" for c in criteria]
            formula = "(" + ") + (".join(formula_parts) + ")"
            st.code(f"- {alt}: {formula} = {total_scores[alt]:.0f}")

        # Buat DataFrame hasil
        result_df = pd.DataFrame({
            "Vendor": alternatives,
            "Skor": [copeland_scores[alt] for alt in alternatives]
        }).sort_values(by="Skor", ascending=False).reset_index(drop=True)

        # Tambahkan peringkat dengan emoji
        medals = ["🥇 Pertama", "🥈 Kedua", "🥉 Ketiga"]
        result_df["Peringkat"] = [medals[i] if i < len(medals) else f"Ke-{i+1}" for i in range(len(result_df))]

        st.markdown("**Skor Copeland:**")
        st.dataframe(result_df)

if __name__ == "__main__":
    main()
