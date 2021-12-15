from Connected_Components import ConectedComponents

import unittest

class TestConnectedComponets(unittest.TestCase):
    def test1(self):
        cc=ConectedComponents(5)
        cc.addEdge(0,1)
        cc.addEdge(1,2)
        cc.addEdge(3,4)
        x=cc.num_connected_components()
        self.assertEqual(x, 2)

    def test2(self):
        cc = ConectedComponents(5)
        cc.addEdge(0, 1)
        cc.addEdge(1, 2)
        cc.addEdge(2, 3)
        cc.addEdge(3, 4)
        x = cc.num_connected_components()
        self.assertEqual(x, 1)

    def test3(self):
        cc = ConectedComponents(5)
        x = cc.num_connected_components()
        self.assertEqual(x,5)

    def test4(self):
        cc = ConectedComponents(0)
        x = cc.num_connected_components()
        self.assertEqual(x,0)

    def test5(self):
        cc = ConectedComponents(3)
        cc.addEdge(0, 1)
        cc.addEdge(0, 2)
        cc.addEdge(0, 1)
        x = cc.num_connected_components()
        self.assertEqual(x,1)




if __name__ == '__main__':

    unittest.main()