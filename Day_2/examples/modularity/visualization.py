import matplotlib.pyplot as plt
import seaborn as sns

def plot_final_grades(df, name_col='Name', score_col='Final Score'):
    df_sorted = df.sort_values(by=score_col, ascending=False)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(
        data=df_sorted, 
        x=score_col, 
        y=name_col, 
        palette='viridis'
    )
    
    plt.title('Academic Standing: The 12 Olympians', fontsize=14)
    plt.xlabel('Final Weighted Grade', fontsize=12)
    plt.ylabel('Student', fontsize=12)
    plt.axvline(60, color='red', linestyle='--', label='Passing Threshold')
    plt.legend()
    plt.tight_layout()
    plt.show(block=False)

def plot_effort_vs_performance(df, hw_col='hw_average', exam_col='exam_average', name_col='Name'):
    plt.figure(figsize=(10, 6))
    # reference line
    plt.plot([60, 100], [60, 100], color='gray', linestyle='--', alpha=0.5)
    plot = sns.scatterplot(
        data=df, 
        x=hw_col, 
        y=exam_col, 
        hue=name_col, 
        s=200, 
        palette='deep'
    )
    # label points
    for i in range(df.shape[0]):
        plt.text(
            df[hw_col][i]+1, 
            df[exam_col][i]+1, 
            df[name_col][i], 
            fontsize=9
        )

    plt.title('Effort vs Performance)', fontsize=14)
    plt.xlabel('Homework Average (Effort)', fontsize=12)
    plt.ylabel('Exam Average (Performance)', fontsize=12)
    plt.xlim(60, 105)
    plt.ylim(60, 105)
    plt.grid(True, alpha=0.3)
    plt.show()