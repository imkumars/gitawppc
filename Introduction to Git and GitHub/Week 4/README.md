# WEEK 4:
### Pull Request:
			Forking: A way of creating a copy of the given repository so taht it belongs to our user.
			Pull request: A commit or series of commits that you send to the owner of the repository so that they incorporate it into their tree.
			
			R: https://help.github.com/en/articles/about-pull-request-merges
			
			Note:
				What is the difference between using squash and fixup when rebasing?
					Squash combines the commit messages into one. Fixup discards the new commit message.
						The fixup operation will keep the original message and discard the message from the fixup commit, while squash combines them.
						
				Under what circumstances is a new fork created?
					When you want to experiment with changes without affecting the main repository.
						 For instance, when you want to propose changes to someone else's project, or base your own project off of theirs.
						 
				What combination of command and flags will force Git to push the current snapshot to the repo as it is, possibly resulting in permanent data loss?
					git push -f
						 git push with the -f flag forcibly replaces the old commits with the new one and forces Git to push the current snapshot to the repo as it is.
						 This can be dangerous as it can lead to remote changes being permanently lost and is not recommended unless you're pushing fixes to your
						 own fork (nobody else is using it) such as in the case after doing interactive rebasing to squash multiple commits into one as demonstrated.
						 
				When using interactive rebase, which option is the default, and takes the commits and rebases them against the branch we selected?
					pick
						The pick keyword takes the commits and rebases them against the branch we have chosen.
						
						
### Code Review:
			Code review means going through someones else's code or documentation or configuration and checking that it all make sense and follow the expected patterns.
			
			R: http://google.github.io/styleguide/
			R: https://help.github.com/en/articles/about-pull-request-reviews
			R: https://medium.com/osedea/the-perfect-code-review-process-845e6ba5c31
			R: https://smartbear.com/learn/code-review/what-is-code-review/
		
			Note:
				When should we respond to comments from collaborators and reviewers?
					Always.
						It is good manners and proper conduct to respond, even when it's simply an acknowledgement.
						
				
				What is a nit?
					A trivial comment or suggestion
							In git jargon (and elsewhere in the tech world), a nit is a minor “nitpick” about a piece of code.
							
				Common code issues that might be addressed in a code review.
					Using unclear names. Unclear names can make our code hard to understand.
					Forgetting to handle a specific condition. If there is a specific condition that could cause a problem and we don't address it, the result could be catastrophic.
					Forgetting to add tests. Tests are an important addition to our code to ensure it runs smoothly.
					
				If we've pushed a new version since we've made a recent change, what might our comment be flagged as?
					Outdated. If we push a new version after making a change, old comments are marked with the "Outdated" flag.
					
				What are the goals of code review?
					Make sure that the contents are easy to understand
						By reviewing our code, we can identify where we can make our code more clear and easy to understand.
					Ensure consistent style
						By comparing our code to style guidelines, we can keep our style consistent and readable.
					Ensure we don't forget any important cases
						Code review can reveal cases or conditions we need to handle in our code.

### Managing Projects:
			Note: If we mention Closes #<issue_number> in commit message then, this will automatically closes an issue having issue number with <issue_number>
			
			Continuous Integration System (CI): Will build and test our code every time there's a change.
			
			Continuous Deployment / Continuous Delivery (CD): New code is deployed often.
			
			Note: Popular CI/CD tools Jenkins, GitLabs
			
			Pipelines: Specify the steps that need to run to get the result you want.
			
			Artifacts: The name used to describe any files that are generated as part of the pipeline.
			
			R: https://arp242.net/diy.html 
			R: https://help.github.com/en/articles/closing-issues-using-keywords
			R: https://help.github.com/en/articles/setting-guidelines-for-repository-contributors 
			R: https://www.infoworld.com/article/3271126/what-is-cicd-continuous-integration-and-continuous-delivery-explained.html
			R: https://stackify.com/what-is-cicd-whats-important-and-how-to-get-it-right/
			R: https://docs.travis-ci.com/user/tutorial/
			R: https://docs.travis-ci.com/user/build-stages/
			
			Note:
				How do we reference issues in our commits with automatic links?
					By using one of the keywords followed by a hashtag and the issue number.
						Keywords such as closes or resolves followed by a hashtag and the issue number will tell Git to autolink to the issue with the provided ID number.
				
				What is an artifact in terms of continuous integration/continuous delivery (CI/CD) pipelines?
					Any file generated as part of the CI/CD pipeline.
						Artifacts can include compiled code, test results, logs, or any type of file generated as part of the pipeline.
				
				Which of the following statements are good advice for project maintainers? (Check all that apply)
					Reply promptly to pull-requests
						The more time that passes until a pull-request gets reviewed, the more likely it is that there's a new commit that causes a conflict when you try to merge in the change.
					Understand any changes you accept
						Not only do we not know whether the original coder is going to be around to maintain those functions, we also want to avoid feature creep and unmanageable code.
					Use an issue tracker 
						The larger our project grows, the more useful an issue tracker can be for collaborating.
				
				Which statement best represents what a Continuous Integration system will do?
					Run tests automatically
						A continuous integration system will build and test our code every time there's a change. 
						
				Which statement best represents what a Continuous Delivery (CD) system will do?
					Update with incremental rollouts
						Continuous Delivery means new code is often deployed with the goal of avoiding rollouts with lots of changes between two versions.
						
		
		Module Review:
		
