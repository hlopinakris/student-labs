import sys

def catsay(text):
    border = "-" * (len(text) + 2)
    print(f" {border}")
    print(f"< {text} >")
    print(f" {border}")
    
    print(r"""
   /\_/\  
  ( ^.^ ) 
   > ~ <  
  /|   |\ 
 (_|   |_)
    """)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        message = " ".join(sys.argv[1:])
    else:
        message = "Nyan!"
        
    catsay(message)
