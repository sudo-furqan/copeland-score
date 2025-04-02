import streamlit as st
import pandas as pd
import itertools

def calculate_copeland_score(preference_table):
    alternatives = list(preference_table.keys())
    scores = {alt: sum(preference_table[alt]) for alt in alternatives}
    
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
    st.title("Copeland Score Calculator with Preference Table")
    
    # Input alternatives
    alternatives = st.text_area("Enter alternatives (one per line)", "A\nB\nC").split("\n")
    alternatives = [alt.strip() for alt in alternatives if alt.strip()]
    
    if len(alternatives) < 2:
        st.warning("Enter at least two alternatives.")
        return
    
    st.subheader("Preference Table")
    preference_table = {}
    for alt in alternatives:
        preference_table[alt] = [st.number_input(f"Preference score for {alt} from DM {i+1}", value=0, step=1, key=f"score_{alt}_{i}") for i in range(3)]
    
    if st.button("Calculate Copeland Score"):
        final_scores = calculate_copeland_score(preference_table)
        df = pd.DataFrame(list(final_scores.items()), columns=["Alternative", "Score"])
        df = df.sort_values(by="Score", ascending=False)
        st.subheader("Results")
        st.dataframe(df)

if __name__ == "__main__":
    main()
