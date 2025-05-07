dic={
    "nayan": "hushar mulga ahe",
    "sham" : "tiger"
}
print(dic["nayan"])
print(dic.get("nayan2"))

print(dic.items())
for key, value in dic.items():
    print("the value corresponding to the key{key} is {value}")