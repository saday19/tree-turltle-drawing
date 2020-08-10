import turtle

def getRules():
    gettingRules = True
    rules = []
    
    while gettingRules:
        inp = input("Enter new rule 'LHS -> RHS' (empty line to exit): ")
        if inp != "":
            rules.append(inp)
        else:
            gettingRules = False

    print(rules)
    return rules

def createLSystem(iterations, axiom):
    creatingRules = True
    newAxiom = ""
    ruleset = getRules()
    
    for i in range(iterations):
        axiom = applyRules(axiom, ruleset)
    
    print(axiom)
    return axiom

def applyRules(axiom, rules):
    
    result = ""
    
    for c in axiom:
        applied = False
        for r in rules:
            currentRule = splitRule(r)
            if currentRule[0] == c:
                result = result + currentRule[1]
                applied = True
        if applied == False:
            result = result + c
            
    return result

def splitRule(rule):
    
    loc = rule.find(" -> ")
    finalRule = [rule[0:loc], rule[loc+4:len(rule)]]
    
    return finalRule

def drawLSystem(t, angle, length, instructions):
    
    size = 1
    saves = []

    for c in instructions:
        if c == 'F':
            t.forward(length)
        elif c == 'B':
            t.forward(-length)
        elif c == '+':
            t.right(angle)
        elif c == '-':
            t.left(angle)
        elif c == '>':
            size = size + 1
            t.pensize(size)
        elif c == '<':
            size = size - 1
            t.pensize(size)
        elif c == "[":
            currentSave = [t.xcor(), t.ycor(), t.heading(), size]
            saves.append(currentSave)
        elif c == "]":
            currentSave = saves.pop()
            t.pu()
            t.setpos(currentSave[0], currentSave[1])
            t.setheading(currentSave[2])
            t.pd()
            size = currentSave[3]

def main():
    print("""
    Symbols: 'F'=MoveForward, 
             'B'=MoveBackward, 
             '+'=TurnRight, 
             '-'=TurnLeft, 
             '>'=PenWider, 
             '<'=PenNarrower, 
             '['=StateSave, 
             ']'=StateRestore,
             'ACDEGHIJKLMNOPQRSTUVWXYZ'=TurtleIgnores
    """)

    iterations = int(input("Enter iterations: "))
    length = int(input("Enter length: "))
    angle = float(input("Enter angle: "))
    axiom = input("Enter axiom: ")
    
    lSystem = createLSystem(iterations, axiom)

    turt = turtle.Turtle()
    turt.speed(9)
    turt.ht()
    wn = turtle.Screen()
    drawLSystem(turt, angle, length, lSystem)

    
if __name__ == "__main__":
    main()
