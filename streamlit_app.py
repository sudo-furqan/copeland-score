import streamlit as st
import pandas as pd
import itertools

def calculate_copeland_score(comparisons, alternatives):
    scores = {alt: 0 for alt in alternatives}
    
    for (alt1, alt2), result in comparisons.items():
        if result == alt1:
            scores[alt1] += 1
            scores[alt2] -= 1
        elif result == alt2:
            scores[alt2] += 1
            scores[alt1] -= 1
        # If draw, no change in scores
    
    return scores

def main():
    st.title("Copeland Score Calculator")
    
    # Input alternatives
    alternatives = st.text_area("Enter alternatives (one per line)", "A\nB\nC").split("\n")
    alternatives = [alt.strip() for alt in alternatives if alt.strip()]
    
    if len(alternatives) < 2:
        st.warning("Enter at least two alternatives.")
        return
    
    st.subheader("Pairwise Comparisons")
    comparisons = {}
    
    for alt1, alt2 in itertools.combinations(alternatives, 2):
        result = st.radio(f"Who wins between {alt1} and {alt2}?", (alt1, alt2, "Draw"), key=f"{alt1}-{alt2}")
        comparisons[(alt1, alt2)] = result
    
    if st.button("Calculate Copeland Score"):
        scores = calculate_copeland_score(comparisons, alternatives)
        df = pd.DataFrame(list(scores.items()), columns=["Alternative", "Score"])
        df = df.sort_values(by="Score", ascending=False)
        st.subheader("Results")
        st.dataframe(df)

if __name__ == "__main__":
    main()
