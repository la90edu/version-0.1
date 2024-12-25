import time
begin_count=0

def begin():
    global begin_count
    begin_count= time.time()
    
def end():
    end_count=time.time()
    delta=begin_count-end_count
    answer=abs(round(delta,2))
    return (answer)
    #print(answer)
    
begin()
time.sleep(2)
end()

    