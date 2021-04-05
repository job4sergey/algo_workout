from collections import defaultdict


# Idea create synthetic node, which point to every other node in the same group
# when we group[u] != group[v], express edge between u and v
# via edge between group_follower[group[u]] and group_leader[group[v]]
# in case node does not belong to any group, we assign a synthetic group to it
class Solution(object):
    def sortItems(self, n, m, group, beforeItems):
        g = defaultdict(set)

        g_lead = {}  # group leaders
        g_follow = {}
        synth_nodes = set()

        nid = n
        gid = m

        def create_leaders_followers(gid):
            nonlocal nid

            nid += 1
            g_lead[gid] = nid
            synth_nodes.add(nid)
            g[nid] = set()

            nid += 1
            g_follow[gid] = nid
            synth_nodes.add(nid)
            g[nid] = set()

        def build_graphs():
            nonlocal gid
            for g_id in list(range(m)):
                create_leaders_followers(g_id)

            for u in range(n):
                if group[u] == -1:
                    group[u] = gid
                    g_lead[gid] = u
                    g_follow[gid] = u
                    gid += 1

            for u, vs in enumerate(beforeItems):
                for v in vs:
                    if group[u] == group[v]:
                        g[u].add(v)
                    else:
                        g[g_follow[group[u]]].add(g_lead[group[v]])

            for u in range(n):
                if u not in g:
                    g[u] = set()

                if g_lead[group[u]] != u:
                    g[g_lead[group[u]]].add(u)
                    g[u].add(g_follow[group[u]])

        build_graphs()

        def topsort():
            colors = {}
            res = []

            def dfs(u):
                c = colors.get(u, 2)
                if c == 0:
                    return True
                elif c == 1:
                    return False

                colors[u] = 1
                for v in g[u]:
                    if not dfs(v):
                        return False
                colors[u] = 0
                if u not in synth_nodes:
                    res.append(u)

                return True

            for g_id in range(gid):
                if not dfs(g_lead[g_id]):
                    return []

            return res

        return topsort()
