package useful;
//HashMap和HashTable的使用方法
/**
 * ┌─┐       ┌─┐ + +
 * ┌──┘ ┴───────┘ ┴──┐++
 * │                 │
 * │       ───       │++ + + +
 * ███████───███████ │+
 * │                 │+
 * │       ─┴─       │
 * │                 │
 * └───┐         ┌───┘
 * │         │
 * │         │   + +
 * │         │
 * │         └──────────────┐
 * │                        │
 * │                        ├─┐
 * │                        ┌─┘
 * │                        │
 * └─┐  ┐  ┌───────┬──┐  ┌──┘  + + + +
 * │ ─┤ ─┤       │ ─┤ ─┤
 * └──┴──┘       └──┴──┘  + + + +
 */

import java.util.HashMap;
import java.util.Hashtable;
import java.util.concurrent.ConcurrentHashMap;

public class hash {
    public static void main(String[] args) {

        hash hash = new hash();
        hash.testHashMap();
        hash.testHashTable();
    }


    public void testHashMap() {
        /**
         *@描述 线程安全的，可以有null值，在多线程下可以使用ConcurrentHashMap替代.
         *@参数 []
         *@返回值 void
         *@创建时间 2019/4/4
         */
        HashMap<Object, Object> hashmap = new HashMap<>();
        hashmap.put("asdf", 10);
        hashmap.put(10, 20);
        hashmap.put(null, 10);
        hashmap.put(null, 30);
        System.out.println(hashmap);

    }

    public void testHashTable() {
        /**
         *@描述 线程安全的，不允许有空值存在，效率比不上hashmap，一般不建议使用hashmap,遗留类。
         *@参数 []
         *@返回值 void
         *@创建时间 2019/4/4
         */
        Hashtable<Object, Object> hashtable = new Hashtable<>();
        hashtable.put("ddd", 10);
        hashtable.put(10, 20);
//        hashtable.put(null, 10);
//        hashtable.put(null, 30);
        System.out.println(hashtable);
    }

}
