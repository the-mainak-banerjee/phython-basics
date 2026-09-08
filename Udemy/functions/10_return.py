def idle_chaiwala():
    pass

print(idle_chaiwala())

def chai_sold():
    return 200

print(chai_sold())

def chai_status(cupe_left):
    if cupe_left == 0:
        return "Sorry, chai over"
    return "Chai ready"

print(chai_status(0))
print(chai_status(5))

def chai_report():
    return 100,20, 10 

report = chai_report()
print(report)

sold, remaining, _ = chai_report()
print("Sold", sold)
print("remaining", remaining)