import unittest
from dataclasses import dataclass, field
from typing import List


@dataclass
class Creator:
    name: str = ''
    popularity: int = 0
    movies: List[str] = field(default_factory=lambda: [])
    views: List[int] = field(default_factory=lambda: [])


class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        d = {}
        creatorObjs: List[Creator] = []
        for cname, m, v in zip(creators, ids, views):
            c = Creator()
            if cname in d:
                c = d[cname]
            else:
                creatorObjs.append(c)
                c.name = cname
                d[cname] = c

            c.movies.append(m)
            c.views.append(v)
            c.popularity += v

        best_creators = []
        best_creator_views = -1
        for c in creatorObjs:
            if c.popularity == best_creator_views:
                best_creators.append(c.name)
            elif c.popularity > best_creator_views:
                best_creator_views = c.popularity
                best_creators = [c.name]

        ans = []
        for best_creator in best_creators:
            movie_most = -1
            movie = ''
            obj: Creator = d[best_creator]
            for i, v in zip(obj.movies, obj.views):
                if v == movie_most:
                    movie = min(movie, i)
                if v > movie_most:
                    movie_most = v
                    movie = i
            ans.append([best_creator, movie])
        return ans


def test(testObj: unittest.TestCase, creators: List[str], ids: List[str],
         views: List[int], expected: List[List[str]]) -> None:

    so = Solution()

    actual = so.mostPopularCreator(creators, ids, views)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   ["alice", "bob", "alice", "chris"],  [
             "one", "two", "three", "four"],  [5, 10, 5, 4], [["alice", "one"], ["bob", "two"]])

    def test_2(self):
        test(self,   ["alice", "alice", "alice"],  [
             "a", "b", "c"],  [1, 2, 2], [["alice", "b"]])

    def test_3(self):
        test(self,   ["a"],  [
             "a"],  [0], [["a", "a"]])


if __name__ == '__main__':
    unittest.main()

'''

'''
