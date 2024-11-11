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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode res = new ListNode(-1);
        ListNode temp = res;
        while(list1 != null || list2!=null){
            int ans=-1;
            if(list1!=null && list2!=null){
                if(list1.val<=list2.val){
                    ans=list1.val;
                    list1=list1.next;
                }
                else{
                    ans=list2.val;
                    list2=list2.next;
                }
            }
            else if(list1!=null && list2==null){
                ans=list1.val;
                list1=list1.next;
            }
            else{
                ans=list2.val;
                list2=list2.next;
            }
            temp.next= new ListNode(ans);
            temp=temp.next;
        }
        return res.next;
    }
}