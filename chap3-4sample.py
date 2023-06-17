def minutes_to_hours(minutes: float) -> float:
    hours = round(minutes / 60, 2)
    return hours

str_minutes = input("求めたい分を入力してください：")
hours = minutes_to_hours(float(str_minutes))
print(f"{str_minutes}分は{hours}時間です。")
