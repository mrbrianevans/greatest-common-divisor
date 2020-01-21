private static int euclid(int x, int y){
        int m = 0;
        int n = 0;
        if (x < y){
            m = y;
            n = x;
        } else {
            m = x;
            n = y;
        }

        if (n==0){
            return m;
        } else{
            int r = m % n;
            m = n;
            n = r;
            return euclid(m, n);
        }
    }
