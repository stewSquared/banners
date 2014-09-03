import unittest
from flat2iso import *

class Tests(unittest.TestCase):

    def test_init(self):
        size = (1,1)
        self.assertEqual(fresh_grid(size),
                         [list("    "),
                          list("___ ")])
        size = (3,3)
        self.assertEqual(fresh_grid(size),
                         list(map(list,
                                  ["        ",
                                   "_______ ",
                                   "_______ ",
                                   "_______ ",])))

    def test_str_flat(self):
        size = (1,1)
        self.assertEqual(
            to_str(fresh_grid(size)),
            '\n'.join([r"    ",
                       r" ___ "]))

        size = (3,3)
        self.assertEqual(
            to_str(fresh_grid(size)),
            '\n'.join([r"        ",
                       r" _______ ",
                       r"  _______ ",
                       r"   _______ "]))
                   
        
    def test_pop_one(self):
        size = (1,1)
        pos = (0,0)
        self.assertEqual(
            to_str(pop(pos, fresh_grid(size))),
            '\n'.join([r" /\\\ "[:-1],
                       r" \///"]))

        size = (3,3)
        pos = (1,1)
        self.assertEqual(
            to_str(pop(pos, fresh_grid(size))),
            '\n'.join([r"        ",
                       r" ___/\\\ ",
                       r"  __\///_ ",
                       r"   _______ "]))

    def test_ctig_banner(self):
        self.assertEqual(
            from_file("ctig-flat"),
r"""                                                                          
 _______/\\\\\\\\\____/\\\\\\\\\\\\\\\__/\\\\\\\\\\\______/\\\\\\\\\______ 
  _____/\\\///////\\\_\///////\\\/////__\/////\\\///_____/\\\///////\\\____ 
   ___/\\\/______\///________\/\\\___________\/\\\______/\\\/______\///_____ 
    __\/\\\__/\\\\\___________\/\\\___________\/\\\_____\/\\\________________ 
     __\/\\\_\/\\\\\___________\/\\\___________\/\\\_____\/\\\______/\\\\\\\__ 
      __\/\\\_\/////____________\/\\\___________\/\\\_____\/\\\_____\/////\\\__ 
       __\///\\\______/\\\_______\/\\\___________\/\\\_____\///\\\______/\\\/___ 
        ____\///\\\\\\\\\/________\/\\\________/\\\\\\\\\\\___\///\\\\\\\\\/_____ 
         ______\/////////__________\///________\///////////______\/////////_______ """
        )


if __name__ == '__main__':
    unittest.main()
