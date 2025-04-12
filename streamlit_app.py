import streamlit as st
import pandas as pd
import itertools

def calculate_copeland_score(alternatives, weighted_scores):
    copeland_scores = {alt: 0 for alt in alternatives}

    for alt1, alt2 in itertools.combinations(alternatives, 2):
        total1 = sum(weighted_scores[alt1])
        total2 = sum(weighted_scores[alt2])

        if total1 > total2:
            copeland_scores[alt1] += 1
        elif total1 < total2:
            copeland_scores[alt2] += 1
        # draw -> both get 0 (no score change)

    return copeland_scores

def main():
    st.title("Copeland Score Calculator with Criteria and Weights")
    
    # Input criteria and weights
    st.subheader("Define Criteria and Weights (%)")
    criteria_input = st.text_area("Enter criteria (one per line)", "Cost\nQuality\nDurability")
    criteria = [c.strip() for c in criteria_input.split("\n") if c.strip()]
    
    weights = {}
    for criterion in criteria:
        weights[criterion] = st.number_input(f"Weight for {criterion} (%)", min_value=0, max_value=100, value=10, step=1)
    
    total_weight = sum(weights.values())
    if total_weight != 100:
        st.warning("Total weight must sum to 100%.")
        return
    
    # Input alternatives
    st.subheader("Define Alternatives")
    alternatives = st.text_area("Enter alternatives (one per line)", "A\nB\nC").split("\n")
    alternatives = [alt.strip() for alt in alternatives if alt.strip()]
    
    if len(alternatives) < 2:
        st.warning("Enter at least two alternatives.")
        return
    
    # Input preference values
    st.subheader("Enter Alternative Scores")
    weighted_scores = {alt: [] for alt in alternatives}
    for alt in alternatives:
        for criterion in criteria:
            score = st.number_input(f"Score for {alt} on {criterion}", min_value=0, max_value=100, value=50, step=1, key=f"{alt}_{criterion}")
            weighted_scores[alt].append(score * (weights[criterion] / 100))
    
    if st.button("Calculate Copeland Score"):
        final_scores = calculate_copeland_score(alternatives, weighted_scores)
        df = pd.DataFrame(list(final_scores.items()), columns=["Alternative", "Copeland Score"])
        df = df.sort_values(by="Copeland Score", ascending=False)
        st.subheader("Results")
        st.dataframe(df)

if __name__ == "__main__":
    main()
