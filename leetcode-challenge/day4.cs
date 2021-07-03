using System;
using System.Collections;
using System.Collections.Generic;

using System.Linq;

public class HashableList //: IList<int>
{
    public HashableList(int[] list) {
        this.list = list;
    }

    public int[] list { get; set; }

    public override bool Equals(object obj) {
        HashableList other = obj as HashableList;
        if(other == null) return false;
        return list[0] == other.list[0] && list[1] == other.list[1] && list[2] == other.list[2];
    }

    // only uses the first 3 items of the list.
    public override int GetHashCode() {
        if (list == null)
            return 0;
        else {
            int hash = 43;
            hash += hash ^ (19 * list[0].GetHashCode());
            hash += hash ^ (19 * list[1].GetHashCode());
            hash += hash ^ (19 * list[2].GetHashCode());
            return hash;
        } 
    } 
}

class Day4 
{
    const long MAX_NUM = 10*10*10*10*10;
    
    //Dictionary<(int, int, int), bool> taken = new Dictionary<(int, int, int), bool>();
    int[] countOf = new int[MAX_NUM*2 + 1]; // TODO: turn to hashmap
    bool[] inNums = new bool[MAX_NUM*2 + 1];
    
    public IList<IList<int>> ThreeSum(int[] nums) {
        HashSet<HashableList> triplesSet = new HashSet<HashableList>(); 
        
        Array.Sort(nums);

        // setup lookup table
        for(int i = 0; i < nums.Length; i++) {
            inNums[nums[i] + MAX_NUM] = true;
            countOf[nums[i] + MAX_NUM] += 1;
        }
        
        // go through every unique pair
        for (int i = 0; i < nums.Length; i++) {
            for (int j = 0; j < i; j++) {
                int complement = -(nums[i] + nums[j]);
                
                if (complement > MAX_NUM) {
                    break;
                }
                else if (complement < -MAX_NUM || !inNums[complement + MAX_NUM])
                    continue;

                if (countOf[complement + MAX_NUM] < 1 + (complement == nums[j] ? 1 : 0) + (complement == nums[i] ? 1 : 0))
                    continue;

                triplesSet.Add(MakeSortedTriple(nums[i], nums[j], complement));
                
                
            }
        }

        return new List<IList<int>>(triplesSet.Select(x => x.list).ToList());
    }

    private HashableList MakeSortedTriple(int a, int b, int c) {
        //return new int[] {a, b, c};
        var list = new int[] {a, b, c};
        TinySort(list); // this sort is overkill--> I should use insertion sort or something.
        return new HashableList(list);
    }

    private void TinySort(int[] list) {
        for (int i = 0; i < 2; i++) {
            if (list[i+1] < list[i]) {
                int tmp = list[i];
                list[i] = list[i+1];
                list[i+1] = tmp;
            }
        }
        for (int i = 0; i < 1; i++) {
            if (list[i+1] < list[i]) {
                int tmp = list[i];
                list[i] = list[i+1];
                list[i+1] = tmp;
            }
        }
    }
};

public class Testing 
{
    public static void Main() {
        var instance = new Day4();
        var list = new int[] {-1,0,1,2,-1,-4};
        var triples = instance.ThreeSum(list);

        PrintListOfList(triples);
        Console.WriteLine("=========");

        var instance2 = new Day4();
        var list2 = new int[100];
        for (int i = 0; i < 100; i++) {
            list2[i] = (i-50);
        }
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
