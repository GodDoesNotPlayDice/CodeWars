# You are given two vectors starting from the origin (x=0, y=0) with coordinates (x1,y1) and (x2,y2). Your task is to find out if these vectors are collinear. Collinear vectors are vectors that lie on the same straight line. They can be directed in the same or opposite directions. One vector can be obtained from another by multiplying it by a certain number. In terms of coordinates, vectors (x1, y1) and (x2, y2) are collinear if (x1, y1) = (k*x2, k*y2) , where k is any number acting as a coefficient.

def collinearity(x1, x2, y1, y2)
    if (x1 > 1000 or x1 < -1000)
        return false
    end
    if (x2 > 1000 or x2 < -1000)
        return false
    end
    if (y1 > 1000 or y1 < -1000)
        return false
    end
    if (y2 > 1000 or y2 < -1000)
        return false
    end

    if (x1 == 0 and y1 == 0) or (x2 == 0 and y2 == 0)
        return true
    end

    if x2 == 0
        x1 = 0
    elsif y2 == 0
        y2 = 0
    end


    if (x1 * y2) == (y1 * x2)
        return true
    else
        return false
    end
end

puts collinearity(587, 0, 439, -844)