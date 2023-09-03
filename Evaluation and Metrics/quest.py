import pandas as pd
import warnings
warnings.filterwarnings("ignore")

#1 Which user has the highest MAE?
print("1. Which user has the highest MAE?")
users=pd.read_csv("by_user.csv")
maes=users.sort_values(by="MAE",ascending=False)
print(maes[["User","MAE"]].iloc[0,0])
print("\n")

#2 What is the MAE for this highest-MAE user?
print("2. What is the MAE for this highest-MAE user?")
print(maes[["User","MAE"]].iloc[0,1])
print("\n")

#3 Which user has the lowest MAE?
print("3. Which user has the lowest MAE?")
print(maes[["User","MAE"]].iloc[9,0])
print("\n")

#4 What is the MAE for this lowest-MAE user?
print("4. What is the MAE for this lowest-MAE user?")
print(maes[["User","MAE"]].iloc[9,1])
print("\n")

#5 Which movie has the highest MAE?
print("5. Which movie has the highest MAE?")
movies=pd.read_csv("by_movie.csv")
maes=movies.sort_values(by="MAE",ascending=False)
print(maes[["Movie","MAE"]].iloc[0,0])
print("\n")

#6 What is the MAE for this highest-MAE movie (3 decimal places)?
print("6. What is the MAE for this highest-MAE movie?")
print(round(maes[["Movie","MAE"]].iloc[0,1],3))
print("\n")

#7 Which movie has the lowest MAE?
print("7. Which movie has the lowest MAE?")
print(maes[["Movie","MAE"]].iloc[9,0])
print("\n")

#8 What is the MAE for this lowest-MAE movie (3 decimal places)?
print("8. What is the MAE for this lowest-MAE movie?")
print(round(maes[["Movie","MAE"]].iloc[9,1],3))
print("\n")

#9 Overall MAE score across all predictions (3 decimal places)
print("9. Overall MAE score across all predictions (3 decimal places)")
metrics=pd.read_csv("overall_metrics.csv")
print(round(metrics.iloc[0,0],3))
print("\n")

#10 MAE by-user (3 decimal places)
print("10. MAE by-user")
print(round(metrics.iloc[0,1],3))
print("\n")

#11 MAE by-movie (3 decimal places)
print("11. MAE by-movie")
print(round(metrics.iloc[0,2],3))
print("\n")

#12 Which user has the highest RMSE?
print("12. Which user has the highest RMSE?")
rmses=users.sort_values(by="RMSE",ascending=False)
print(rmses[["User","RMSE"]].iloc[0,0])
print("\n")

#13  And what is the RMSE for this highest-RMSE user?
print("13. And what is the RMSE for this highest-RMSE user?")
print(round(rmses[["User","RMSE"]].iloc[0,1],3))
print("\n")

#14 Which user has the lowest RMSE?
print("14. Which user has the lowest RMSE?")
print(rmses[["User","RMSE"]].iloc[9,0])
print("\n")

#15  And what is the RMSE for this lowest-RMSE user?
print("15. And what is the RMSE for this lowest-RMSE user?")
print(round(rmses[["User","RMSE"]].iloc[9,1],3))
print("\n")

#16 Overall RMSE to 3 decimals
print("16.Overall RMSE to 3 decimals")
print(round(metrics.iloc[0,4],3))
print("\n")

#17 What user had the highest correlation between ratings and predictions?
print("17. What user had the highest correlation between ratings and predictions?")
corrs=users.sort_values(by="corr",ascending=False)
print(corrs[["User","corr"]].iloc[0,0])
print("\n")

#18 And what is that correlation value (3 decimal places)?
print("18. And what is that correlation value?")
print(round(corrs[["User","corr"]].iloc[0,1],3))
print("\n")

#19 And which user has the lowest correlation?
print("19. And which user has the lowest correlation?")
print(corrs[["User","corr"]].iloc[9,0])
print("\n")

#20 And what is that correlation value (3 decimal places)?
print("20. And what is that correlation value?")
print(round(corrs[["User","corr"]].iloc[9,1],3))
print("\n")

#21 What is the average overall correlation?
print("21. What is the average overall correlation?")
print(round(metrics.iloc[0,5],3))
