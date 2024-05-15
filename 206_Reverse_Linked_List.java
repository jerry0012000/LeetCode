/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        // System.out.println(head.val);
        if (head == null) {
            return null;
        }
        int count = 0;//要添加几个节点就遍历多少次
        ListNode countList = head;//创建一个新链表，从里面抠末位出来
        ListNode temp = new ListNode(0);//添加哑节点
        ListNode reversedList = temp;//指向首节点
        while (countList != null) {
            countList = countList.next;
            count++;
        }
        System.out.println("要添加 " + count + " 个节点");
        // temp.next = countList;
        countList = head;//复原
        int loopNum = count;
        for (int i=0; i<loopNum; i++) {
            countList = head;
            for (int j=1;j<count;j++) {
                countList = countList.next;
            }
            countList.next = null;
            ListNode newListNode = countList;
            temp.next = newListNode;
            temp = temp.next;//当前节点向后移动
            count--;
        }
        temp = reversedList;//指向首节点
        System.out.println("countList: " + countList.val);
        return temp.next;//忽略首节点
    }
}
