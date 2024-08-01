import streamlit as st
from vecs import Vector, Line, point_in_line, line_with_points, angle_between_vectors, point_of_intersection,Plane_alg,Plane_with_points,line_intersect_plane

st.title("3D Geometry Calculator")

# Dropdown menu for selecting functions
option = st.selectbox(
    "Select a function",
    ["Angle Between Vectors", 
     "Point in Line", 
     "Line with Points", 
     "Point of Intersection of 2 lines", 
     "Minimum Distance Between Lines",
     "Plane from Points",
     "Line intersecting Plane"]
)

if option == "Angle Between Vectors":
    st.header("Angle Between Vectors")

    st.subheader("Vector 1")
    col1, col2, col3 = st.columns(3)
    with col1:
        x1 = st.number_input("x1", value=0.0)
    with col2:
        y1 = st.number_input("y1", value=0.0)
    with col3:
        z1 = st.number_input("z1", value=0.0)

    st.subheader("Vector 2")
    col4, col5, col6 = st.columns(3)
    with col4:
        x2 = st.number_input("x2", value=0.0)
    with col5:
        y2 = st.number_input("y2", value=0.0)
    with col6:
        z2 = st.number_input("z2", value=0.0)

    if st.button("Calculate Angle"):
        v1 = Vector(x1, y1, z1)
        v2 = Vector(x2, y2, z2)
        angle_deg, angle_rad = angle_between_vectors(v1, v2)
        st.write(f"Angle: {angle_deg:.2f} degrees")
        st.write(f"Angle: {angle_rad:.2f} radians")

elif option == "Point in Line":
    st.header("Point in Line")

    st.subheader("Point")
    col1, col2, col3 = st.columns(3)
    with col1:
        x = st.number_input("x", value=0.0)
    with col2:
        y = st.number_input("y", value=0.0)
    with col3:
        z = st.number_input("z", value=0.0)

    st.subheader("Line")
    col4, col5, col6 = st.columns(3)
    with col4:
        x1 = st.number_input("Point x1", value=0.0)
    with col5:
        y1 = st.number_input("Point y1", value=0.0)
    with col6:
        z1 = st.number_input("Point z1", value=0.0)

    col7, col8, col9 = st.columns(3)
    with col7:
        dx = st.number_input("Direction dx", value=0.0)
    with col8:
        dy = st.number_input("Direction dy", value=0.0)
    with col9:
        dz = st.number_input("Direction dz", value=0.0)

    if st.button("Check Point"):
        pt = [x, y, z]
        line = Line(Vector(x1, y1, z1), Vector(dx, dy, dz))
        result = point_in_line(pt, line)
        st.write("Point is on the line:" if result else "Point is not on the line")

elif option == "Line with Points":
    st.header("Line with Points")

    st.subheader("Point 1")
    col1, col2, col3 = st.columns(3)
    with col1:
        x1 = st.number_input("x1", value=0.0)
    with col2:
        y1 = st.number_input("y1", value=0.0)
    with col3:
        z1 = st.number_input("z1", value=0.0)

    st.subheader("Point 2")
    col4, col5, col6 = st.columns(3)
    with col4:
        x2 = st.number_input("x2", value=0.0)
    with col5:
        y2 = st.number_input("y2", value=0.0)
    with col6:
        z2 = st.number_input("z2", value=0.0)

    if st.button("Create Line"):
        line = line_with_points([x1, y1, z1], [x2, y2, z2])
        st.write(f"Line: {line}")

elif option == "Point of Intersection of 2 lines":
    st.header("Point of Intersection of 2 lines")

    st.subheader("Line 1")
    col1, col2, col3 = st.columns(3)
    with col1:
        x1 = st.number_input("Point x1", value=0.0)
    with col2:
        y1 = st.number_input("Point y1", value=0.0)
    with col3:
        z1 = st.number_input("Point z1", value=0.0)

    col4, col5, col6 = st.columns(3)
    with col4:
        dx1 = st.number_input("Direction dx1", value=0.0)
    with col5:
        dy1 = st.number_input("Direction dy1", value=0.0)
    with col6:
        dz1 = st.number_input("Direction dz1", value=0.0)

    st.subheader("Line 2")
    col7, col8, col9 = st.columns(3)
    with col7:
        x2 = st.number_input("Point x2", value=0.0)
    with col8:
        y2 = st.number_input("Point y2", value=0.0)
    with col9:
        z2 = st.number_input("Point z2", value=0.0)

    col10, col11, col12 = st.columns(3)
    with col10:
        dx2 = st.number_input("Direction dx2", value=0.0)
    with col11:
        dy2 = st.number_input("Direction dy2", value=0.0)
    with col12:
        dz2 = st.number_input("Direction dz2", value=0.0)

    if st.button("Find Intersection"):
        line1 = Line(Vector(x1, y1, z1), Vector(dx1, dy1, dz1))
        line2 = Line(Vector(x2, y2, z2), Vector(dx2, dy2, dz2))
        intersection = point_of_intersection(line1, line2)
        if intersection:
            st.write(f"Intersection Point: {intersection}")
        else:
            st.write("No intersection point found.")

elif option == "Minimum Distance Between Lines":
    st.header("Minimum Distance Between Lines")

    st.subheader("Line 1")
    col1, col2, col3 = st.columns(3)
    with col1:
        x1 = st.number_input("Point x1", value=0.0)
    with col2:
        y1 = st.number_input("Point y1", value=0.0)
    with col3:
        z1 = st.number_input("Point z1", value=0.0)

    col4, col5, col6 = st.columns(3)
    with col4:
        dx1 = st.number_input("Direction dx1", value=0.0)
    with col5:
        dy1 = st.number_input("Direction dy1", value=0.0)
    with col6:
        dz1 = st.number_input("Direction dz1", value=0.0)

    st.subheader("Line 2")
    col7, col8, col9 = st.columns(3)
    with col7:
        x2 = st.number_input("Point x2", value=0.0)
    with col8:
        y2 = st.number_input("Point y2", value=0.0)
    with col9:
        z2 = st.number_input("Point z2", value=0.0)

    col10, col11, col12 = st.columns(3)
    with col10:
        dx2 = st.number_input("Direction dx2", value=0.0)
    with col11:
        dy2 = st.number_input("Direction dy2", value=0.0)
    with col12:
        dz2 = st.number_input("Direction dz2", value=0.0)

    if st.button("Calculate Distance"):
        line1 = Line(Vector(x1, y1, z1), Vector(dx1, dy1, dz1))
        line2 = Line(Vector(x2, y2, z2), Vector(dx2, dy2, dz2))
        distance = line1.min_distance(line2)
        st.write(f"Minimum Distance: {distance:.2f}")

elif option == "Plane from Points":
    st.subheader("Plane from Points")
    st.subheader("Point 1")
    col1, col2, col3 = st.columns(3)
    with col1:
        x1 = st.number_input("Point x1", value=0.0)
    with col2:
        y1 = st.number_input("Point y1", value=0.0)
    with col3:
        z1 = st.number_input("Point z1", value=0.0)
    st.subheader("Point 2")
    col4, col5, col6 = st.columns(3)
    with col4:
        dx1 = st.number_input("Point x2", value=0.0)
    with col5:
        dy1 = st.number_input("Point y2", value=0.0)
    with col6:
        dz1 = st.number_input("Point z2", value=0.0)
    st.subheader("Point 3")
    col7, col8, col9 = st.columns(3)
    with col7:
        x2 = st.number_input("Point x3", value=0.0)
    with col8:
        y2 = st.number_input("Point y3", value=0.0)
    with col9:
        z2 = st.number_input("Point z3", value=0.0)

    if st.button("Get Algebric equation"):
        plane = Plane_with_points(Vector(x1,y1,z1),Vector(dx1,dy1,dz1),Vector(x2,y2,z2))
        st.write(f"Equation Of Plane: {plane}")

elif option == "Line intersecting Plane":

    st.subheader("Line intersecting Plane")
    option1 = st.selectbox(
    "Select a function",
    [
        "With 3 Points of Plane",
        "With Algebric Equation of Plane"
    ])
    if option1 == "With 3 Points of Plane":

        st.subheader("Point 1")
        col1, col2, col3 = st.columns(3)
        with col1:
            x1 = st.number_input("Point x1", value=0.0)
        with col2:
            y1 = st.number_input("Point y1", value=0.0)
        with col3:
            z1 = st.number_input("Point z1", value=0.0)
        st.subheader("Point 2")
        col4, col5, col6 = st.columns(3)
        with col4:
            dx1 = st.number_input("Point x2", value=0.0)
        with col5:
            dy1 = st.number_input("Point y2", value=0.0)
        with col6:
            dz1 = st.number_input("Point z2", value=0.0)
        st.subheader("Point 3")
        col7, col8, col9 = st.columns(3)
        with col7:
            x2 = st.number_input("Point x3", value=0.0)
        with col8:
            y2 = st.number_input("Point y3", value=0.0)
        with col9:
            z2 = st.number_input("Point z3", value=0.0)
        
        plane = Plane_with_points(Vector(x1,y1,z1),Vector(dx1,dy1,dz1),Vector(x2,y2,z2))

        
        st.subheader("Line Equation")
        aaa, bbb, ccc = st.columns(3)
        with aaa:
            p1 = st.number_input("Point p1", value=0.0)
        with bbb:
            p2 = st.number_input("Point p2", value=0.0)
        with ccc:
            p3 = st.number_input("Point p3", value=0.0)
        
        aa, bb, cc = st.columns(3)
        with aa:
            dd1 = st.number_input("Point dir1", value=0.0)
        with bb:
            dd2 = st.number_input("Point dir2", value=0.0)
        with cc:
            dd3 = st.number_input("Point dir3", value=0.0)

        line = Line(Vector(p1,p2,p3),Vector(dd1,dd2,dd3))

        pt = line_intersect_plane(plane,line)
        if st.button("Get Algebric equation"):
            st.write(f"Point of Intersection: {pt}")

    
    elif option1 == "With Algebric Equation of Plane":

        st.subheader("Plane Algebric Equation")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            x = st.number_input("X", value=0.0)
        with col2:
            y = st.number_input("Y", value=0.0)
        with col3:
            z = st.number_input("Z", value=0.0)
        with col4:
            sol = st.number_input("Solution", value=0.0)

        plane = Plane_alg(x,y,z,sol)

        st.subheader("Line Equation")
        aaa, bbb, ccc = st.columns(3)
        with aaa:
            p1 = st.number_input("Point p1", value=0.0)
        with bbb:
            p2 = st.number_input("Point p2", value=0.0)
        with ccc:
            p3 = st.number_input("Point p3", value=0.0)
        
        aa, bb, cc = st.columns(3)
        with aa:
            dd1 = st.number_input("Point dir1", value=0.0)
        with bb:
            dd2 = st.number_input("Point dir2", value=0.0)
        with cc:
            dd3 = st.number_input("Point dir3", value=0.0)

        line = Line(Vector(p1,p2,p3),Vector(dd1,dd2,dd3))

        pt = line_intersect_plane(plane,line)
        if st.button("Get Algebric equation"):
            st.write(f"Point of Intersection: {pt}")