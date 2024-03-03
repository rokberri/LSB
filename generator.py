class Generator:
    def __init__(self, a, b, c, d, m):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.m = m
    
    
    def generate_num_cycle(self, am_of_int, default_num=0)->int:
        res = 0
        if default_num == 0:
            res = self.a + self.b + self.c + self.d + self.m
        else:
            res  = default_num
        for i in range(am_of_int+1):
            # print(f"Part:{i}--{res}")
            if not i == 0: 
                res = (self.a*(res**3) + self.b*(res**2) + 
                        self.c * res + self.d) % self.m
        return res
            
    def generate_list(self, size)->list[int]:
        result = list()
        item = 0
        for i in range(1,size):
            # print(f"STAGE:{i}--{item}")
            item = self.generate_num_cycle(i,item)
            result.append(item)
        return result
    