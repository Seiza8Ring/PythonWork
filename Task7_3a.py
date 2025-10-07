# Challenge Task: Triangle Area Calculator

tri_count = int(input("How many Triangles? "))
total_area = 0

for i in range(tri_count):
    # number triangle
    print(f"Triangle {i+1}")

    #calculate
    base = int(input("Enter Base: "))
    height = int(input("Enter Height: "))
    area = base * height * 0.5
    total_area += area
    print(f"Area: {area}")

    #add a space
    print(" ")
    
#print total area
print(f'Total area of all triangles: {total_area}')
