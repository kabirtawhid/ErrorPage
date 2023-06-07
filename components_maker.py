# This Program will automatically make components for React 

import sys
from string import Template


def main():
  
  components = sys.argv[1:]
  snippet = Template("""
const $name = () => {
  return (
    <div>
      
    </div>
  );
};

export default $name;
""")
                  
  for component in components:
    code = snippet.substitute(name = component)
    filename = component + '.jsx'
    file = open(filename, 'w')
    file.write(code)
  

if __name__ == '__main__':
  main()