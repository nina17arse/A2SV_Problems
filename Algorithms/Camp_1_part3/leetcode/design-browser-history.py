class ListNode:
    def __init__(self,val,prev=None,next=None):
        self.val=val
        self.prev=prev
        self.next=next
class BrowserHistory:

    def __init__(self, homepage: str):
        self.new=ListNode(homepage)

        

    def visit(self, url: str) -> None:
        self.new.next=ListNode(url,self.new)
        self.new=self.new.next

        

    def back(self, steps: int) -> str:
        while self.new.prev and steps > 0:
            self.new=self.new.prev
            steps-=1
        return self.new.val

        

    def forward(self, steps: int) -> str:
        while self.new.next and steps > 0:
            self.new=self.new.next
            steps-=1
        return self.new.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)