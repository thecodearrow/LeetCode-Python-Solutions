class Solution:
    def minCameras(self,node,hasCamera,parentHasCamera,dp):
        if(node is None):
            #base case! 
            if(hasCamera):
                #cannot be covered!
                return float("inf")
            return 0

        key=(node,hasCamera,parentHasCamera)
        if(key in dp):
            return dp[key]

        if(hasCamera):
            leftCams=min(self.minCameras(node.left,True,True,dp),self.minCameras(node.left,False,True,dp)) 
            rightCams=min(self.minCameras(node.right,True,True,dp),self.minCameras(node.right,False,True,dp)) 
            dp[key]=1+leftCams+rightCams #current node has a camera
            
        else:
            #current node does not have a camera
            if(parentHasCamera):
                #case 2A
                leftCams=min(self.minCameras(node.left,True,False,dp),self.minCameras(node.left,False,False,dp)) #parent will not have camera
                rightCams=min(self.minCameras(node.right,True,False,dp),self.minCameras(node.right,False,False,dp)) #parent will not have camera
                dp[key]= leftCams+rightCams
            else:
                #case 2B
                #otherwise we have to force one child to have a camera!  
                #force left child
                choice1=self.minCameras(node.left,True,False,dp)+min(self.minCameras(node.right,True,False,dp),self.minCameras(node.right,False,False,dp))
                #force right child
                choice2=self.minCameras(node.right,True,False,dp)+min(self.minCameras(node.left,True,False,dp),self.minCameras(node.left,False,False,dp))
                dp[key]= min(choice1,choice2)
        return dp[key]
      

        


    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        if(root is None):
            return 0
        
        if(root.left is None and root.right is None):
            #single node!
            return 1
        

        parentHasCamera=False
        return min(self.minCameras(root,True,parentHasCamera,{}),self.minCameras(root,False,parentHasCamera,{}))
