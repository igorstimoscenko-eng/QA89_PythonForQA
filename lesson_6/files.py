with open("test.txt","w",encoding="utf-8") as file:
    file.write("Hello auto tests!")

#file = open(.........)
#file.close()

# 'r'-> read
# 'w' -> write
# 'a' -> append
# 'r'-> read
# 'w' -> write
# 'a' -> append
# 'r +' read and write
# 'rb','wb'->pdf, screenshots

def log_test_res(test_name,status):
    with open("test_run.log","a",encoding="utf-8") as log_file:
        log_file.write(f"{test_name}:{status}\n")

log_test_res("test_login","Passed")
log_test_res("test_registration","Failed")
log_test_res("test_logout","Failed")