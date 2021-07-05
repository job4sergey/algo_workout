package com.lsa.letcode.the200.numberOfIslands;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static java.util.Arrays.asList;

class Solution3 {
    int connect(char[][] gr, Map<List<Integer>, UFO> cs2ufo, UFO ufo0, int r1, int c1) {
        var rc = gr.length;
        var cc = gr[0].length;

        if (r1 < 0 || r1 >= rc || c1 < 0 || c1 >= cc || gr[r1][c1] == '0') {
            return 0;
        }

        return UFO.union(ufo0, cs2ufo.get(asList(r1, c1)));
    }

    public int numIslands(char[][] gr) {
        var rc = gr.length;
        var cc = gr[0].length;
        var cs2ufo = new HashMap<List<Integer>, UFO>();

        var cn = 0;

        for (var r = 0; r < rc; ++r) {
            for (var c = 0; c < cc; ++c) {
                if (gr[r][c] == '0') {
                    continue;
                }

                var ufo = new UFO();
                cs2ufo.put(asList(r, c), ufo);

                cn += 1;

                cn -= connect(gr, cs2ufo, ufo, r - 1, c);
                cn -= connect(gr, cs2ufo, ufo, r, c - 1);
            }
        }

        return cn;
    }

    static class UFO {
        UFO parent;
        int sz = 1;

        UFO() {
            parent = this;
        }

//        UFO parent() {
//            var p = parent;
//
//            if (parent != this) {
//                parent = parent.parent();
//            }
//
//            return parent;
//        }

        UFO parent() {
            var p = parent;

            while (p.parent != p) {
                p.parent = p.parent.parent;
                p = p.parent;
            }
            parent = p;

            return p;
        }

        static int union(UFO s1, UFO s2) {
            s1 = s1.parent();
            s2 = s2.parent();

            if (s1 == s2) {
                return 0;
            }

            if (s1.sz > s2.sz) {
                s2.parent = s1;
                s1.sz += s2.sz;
            } else {
                s1.parent = s2;
                s2.sz += s1.sz;
            }

            return 1;
        }
    }
}