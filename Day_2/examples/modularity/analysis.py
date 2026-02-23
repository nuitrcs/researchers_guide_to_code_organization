def get_final_score(df, col1, col2, alpha_1):
    final_score = (df[col1] * alpha_1) + (df[col2] * (1-alpha_1))
    return final_score

def rank_students(df):
    ranked_df = df[['Name', 'Final Score']].sort_values(by='Final Score', ascending=False)
    return ranked_df