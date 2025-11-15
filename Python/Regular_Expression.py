import re
pattern=r"Hello"
message1="Hello Developers"
print(re.match(pattern,message1))

message="Deve Hello lopers "
print(re.search(pattern,message))


pattern2=r"\d"
message2="123Hello3Developers78"
print(re.findall(pattern2,message2))

pattern2=r"\d+"
message2="123Hello3Developers78"
print(re.findall(pattern2,message2))


