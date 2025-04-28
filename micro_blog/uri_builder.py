
def mc_parser(fname: str):
    try:
        with open(fname) as f:
            lines = f.readlines()
            for l in lines:
                if l.startswith('uri:'):
                    return l[5:]
    except Exception() as e:
        print(e)
        return ''
        
if __name__ == "__main__":
    print(mc_parser('.\micro_blog\config.txt'))