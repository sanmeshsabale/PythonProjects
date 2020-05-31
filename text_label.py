# Text Labelling

plt.scatter(richest["avg_income"],richest["happyScore"])

plt.text(richest.iloc[0] ["avg_income"],
         richest.iloc[0] ["happyScore"],
         richest.iloc[0] ["country"])
plt.text(richest.iloc[-1] ["avg_income"],
         richest.iloc[-1] ["happyScore"],
         richest.iloc[-1] ["country"])
