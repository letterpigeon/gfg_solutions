from typing import List, Dict, Set
class AlienDictionary:
    def find_order(self, dict: List[str]) -> str:
        if not dict:
            return ''
        if len(dict) == 1:
            return dict[0]

        graph: Dict[str, Set] = self.build_graph(dict)
        return self.dfs(graph)

    def build_graph(self, dict):
        graph = {c: set() for word in dict for c in word}
        for i in range(1, len(dict)):
            current_word, next_word = dict[i-1], dict[i]
            for char1, char2 in zip(current_word, next_word):
                if char1 != char2:
                    graph[char1].add(char2)
                    break

        return graph

    def dfs(self, graph):
        def dfs_helper(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs_helper(neighbor)
            result.append(node)

        result: List[str] = []
        visited: Set[str] = set()

        for node in graph:
            if node not in visited:
                dfs_helper(node)

        return ''.join(result[::-1])

import unittest

class TestAlienDictionary(unittest.TestCase):
    def test_order_of_characters_in_alien_language(self):
        alien_dict = AlienDictionary()
        self.assertEqual(alien_dict.find_order(["wrt", "wrf", "er", "ett", "rftt"]), "wertf")

    def test_single_word(self):
        alien_dict = AlienDictionary()
        self.assertEqual(alien_dict.find_order(["abc"]), "abc")

    def test_no_dependency(self):
        alien_dict = AlienDictionary()
        self.assertEqual(alien_dict.find_order(["a", "b", "c"]), "abc")

    def test_multiple_valid_orders(self):
        alien_dict = AlienDictionary()
        self.assertIn(alien_dict.find_order(["z", "x", "z"]), ["zx", "xz"])

    def test_complex_case(self):
        alien_dict = AlienDictionary()
        self.assertEqual(alien_dict.find_order(["baa", "abcd", "abca", "cab", "cad"]), "bdac")

if __name__ == '__main__':
    unittest.main()
