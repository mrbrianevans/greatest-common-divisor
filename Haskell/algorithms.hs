euclid :: Int -> Int -> Int
-- this might be cleaner with let or where
euclid x y
  | min x y == 0 = max x y
  | otherwise = euclid (min x y) (max x y `mod` min x y)
