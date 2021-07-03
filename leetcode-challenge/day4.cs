using System;
using System.Collections;
using System.Collections.Generic;

public class Day4 {
    const long MAX_NUM = 10*10*10*10*10;
    
    Dictionary<(int, int, int), bool> taken = new Dictionary<(int, int, int), bool>();
    HashSet<int>[] indexof = new HashSet<int>[MAX_NUM*2 + 1];
    bool[] inNums = new bool[MAX_NUM*2 + 1];
    
    public IList<IList<int>> ThreeSum(int[] nums) {
        List<IList<int>> ret = new List<IList<int>>(); 
        
        // setup lookup table
        for(int i = 0; i < nums.Length; i++) {
            inNums[nums[i] + MAX_NUM] = true;
            if (indexof[nums[i] + MAX_NUM] == null)
                indexof[nums[i] + MAX_NUM] = new HashSet<int>();
            indexof[nums[i] + MAX_NUM].Add(i);
        }
        
        // go through every unique pair
        for (int i = 0; i < nums.Length; i++) {
            for (int j = 0; j < i; j++) {
                int complement = -(nums[i] + nums[j]);
                
                if (!inNums[complement + MAX_NUM])
                    continue;

                int containedNums = 0;
                containedNums += indexof[complement + MAX_NUM].Contains(i) ? 1 : 0;
                containedNums += indexof[complement + MAX_NUM].Contains(j) ? 1 : 0;

                if (indexof[complement + MAX_NUM].Count - containedNums > 0 && 
                    !taken.ContainsKey(MakeSortedTuple(nums[i], nums[j], complement))
                ) {
                    ret.Add(MakeTriple(nums[i], nums[j], complement));
                    taken[MakeSortedTuple(nums[i], nums[j], complement)] = true;
                }
            }
        }

        return ret;
    }

    private List<int> MakeTriple(int a, int b, int c) {
        return new List<int>{a, b, c};
    }

    // This tuple is sorted so that a < b < c
    private (int, int, int) MakeSortedTuple(int a, int b, int c) {
        var list = new int[] {a, b, c};
        Array.Sort(list);
        return (list[0], list[1], list[2]);
    }
}

public class Testing {
    public static void Main() {
        var instance = new Day4();
        var list = new int[] {-1,0,1,2,-1,-4};
        var triples = instance.ThreeSum(list);

        PrintListOfList(triples);
        Console.WriteLine("=========");

        var instance2 = new Day4();
        var list2 = new int[] {1, -2, 1, 0, 0};
        var triples2 = instance2.ThreeSum(list2);

        PrintListOfList(triples2);
        Console.WriteLine("=========");

        var instance3 = new Day4();
        var list3 = new int[] {0};
        var triples3 = instance3.ThreeSum(list3);

        PrintListOfList(triples3);
        Console.WriteLine("=========");
    }

    public static void PrintListOfList(IList<IList<int>> metaList) {
        foreach (var sublist in metaList) {
            Console.Write("[ ");
            foreach (var obj in sublist) {
                Console.Write(obj + " ");
            }
            Console.WriteLine("]");
        }
    }
}
