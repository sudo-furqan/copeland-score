import streamlit as st
import pandas as pd
import itertools

def calculate_copeland_score(alternatives, weighted_scores):
    scores = {alt: sum(weighted_scores[alt]) for alt in alternatives}
    
    comparisons = {}
    for alt1, alt2 in itertools.combinations(alternatives, 2):
        if scores[alt1] > scores[alt2]:
            comparisons[(alt1, alt2)] = alt1
        elif scores[alt1] < scores[alt2]:
            comparisons[(alt1, alt2)] = alt2
        else:
            comparisons[(alt1, alt2)] = "Draw"
    
    for (alt1, alt2), result in comparisons.items():
        if result == alt1:
            scores[alt1] += 1
            scores[alt2] -= 1
        elif result == alt2:
            scores[alt2] += 1
            scores[alt1] -= 1
    
    return scores

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
            score = st.number_input(f"Score for {alt} on {criterion}", min_value=0, max_value=100, value=50, step=1)
            weighted_scores[alt].append(score * (weights[criterion] / 100))
    
    if st.button("Calculate Copeland Score"):
        final_scores = calculate_copeland_score(alternatives, weighted_scores)
        df = pd.DataFrame(list(final_scores.items()), columns=["Alternative", "Score"])
        df = df.sort_values(by="Score", ascending=False)
        st.subheader("Results")
        st.dataframe(df)

if __name__ == "__main__":
    main()
