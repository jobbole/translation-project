---
translator: http://www.jobbole.com/members/q3198108035/
reviewer: http://www.jobbole.com/members/hanxiaomax/
via: https://medium.freecodecamp.org/https-explained-with-carrier-pigeons-7029d2193351
---

# **HTTPS explained with carrier pigeons**
# **通过信鸽来解释HTTPS**
![](https://cdn-images-1.medium.com/max/1600/1*vHF6NNdZX9ziiW_uRYzvAA.png)


Cryptography can be a hard subject to understand. It’s full of mathematical proofs. But unless you are actually developing cryptographic systems, much of that complexity is not necessary to understand what is going on at a high level.

密码学可能是一个难以理解的主题。它充满了数学证明。除非你真的需要开发密码系统，否则，如果你只想从宏观的角度了解密码学，你并不需要理解这些复杂的内容。

If you opened this article hoping to create the next HTTPS protocol, I’m sorry to say that pigeons won’t be enough. Otherwise, brew some coffee and enjoy the article.

如果你抱着能够创建下一个 HTTPS 协议的期望打开这篇文章，我不得不遗憾地表示只有信鸽是不够的。否则，煮一些咖啡，享受这篇文章吧。

## **Alice, Bob and … pigeons?**
## **Alice，Bob 和信鸽？**

Any activity you do on the Internet (reading this article, buying stuff on Amazon, uploading cat pictures) comes down to sending and receiving messages to and from a server.

你在互联网上的任何活动（阅读这篇文章，在亚马逊上买东西，上传猫咪的图片）都归结为向服务器发送消息和从服务器接收消息。

This can be a bit abstract so let’s imagine that those messages were delivered by **carrier pigeons**. I know that this may seem very arbitrary, but trust me HTTPS works the same way, albeit a lot faster.

这么讲听起来可能有点抽象，因此，我们不妨假设这些信息是通过**信鸽**传递的。我明白这么假设显得很随意，但请相信我：HTTPS 的工作原理就是这样的，只是快得多。

Also instead of talking about servers, clients and hackers, we will talk about Alice, Bob and Mallory. If this isn’t your first time trying to understand cryptographic concepts you will recognize those names, because they are widely used in technical literature.

本文中我们并不会使用，服务器，客户端和黑客这样的术语，取而代之的是，我们会依次使用人名 Alice、 Bob 和 Mallory来代替它们。如果你不是第一次尝试理解密码概念，你可以认出这些名字，因为它们被广泛用于技术文献中。

## **A first naive communication**
## **一次简单的通讯**
If Alice wants to send a message to Bob, she attaches the message on the carrier pigeon’s leg and sends it to Bob. Bob receives the message, reads it and it’s all is good.
如果 Alice 想要给 Bob 传递一条信息，她将信息绑在信鸽的腿上，然后让信鸽传给 Bob。Bob 收到信息，读取信息。一切都正常。

But what if Mallory intercepted Alice’s pigeon in flight and changed the message? Bob would have no way of knowing that the message that was sent by Alice was modified in transit.
但要是 Mallory 途中拦截了 Alice 的信鸽，并且改变了信息的内容？Bob 无法知道 Alice 发送的信息在传递途中被修改了。

This is how **HTTP** works. Pretty scary right? I wouldn’t send my bank credentials over HTTP and neither should you.
这就是 **HTTP** 的工作原理。挺可怕的，对吧？我不会通过 HTTP 协议来发送我的银行凭证，你也不应该这么做。

## **A secret code**
## **一个密令**
Now what if Alice and Bob are very crafty. They agree that they will write their messages using a secret code. They will shift each letter by 3 positions in the alphabet. For example D → A, E → B, F → C. The plain text message “secret message” would be “pbzobq jbppxdb”.

那如果 Alice 和 Bob 都很机灵呢。他们同意将使用密令来写信息。他们将字母表中的每个字母偏移 3 个位置。比如：D -> A, E -> B, F -> C。明文“secret message”将转换成“pbzobq jbppxdb”。

Now if Mallory intercepts the pigeon she won’t be able to change the message into something meaningful nor understand what it says, because she doesn’t know the code. But Bob can simply apply the code in reverse and decrypt the message where A → D, B → E, C → F. The cipher text “pbzobq jbppxdb” would be decrypted back to “secret message”.

现在，如果 Mallory 拦截了信鸽，她既不能把信息改变成一些有意义的信息，也不能明白信息里说的内容，因为她不知道密令。但是Bob可以简单地反向应用密令（A -> D, B -> E, C -> F）将信息解密。密文“pbzobq jbppxdb”将被解密回“secret message”。


Success!
大功告成！

This is called **symmetric key cryptography**, because if you know how to encrypt a message you also know how to decrypt it.

这被称为**对称密钥密码术**，因为当你知道如何加密一条信息，你也知道如何给信息解密。


The code I described above is commonly known as the **Caesar cipher**. In real life, we use fancier and more complex codes, but the main idea is the same.

我在上面介绍的密令通常被称为**凯撒密码**。在现实生活中，我们使用更高级和复杂的密令，但是主要思路是相同的。

## **How do we decide the key?**
## **我们如何决定密钥是什么？**
Symmetric key cryptography is very secure if no one apart from the sender and receiver know what key was used. In the Caesar cipher, the **key is an offset** of how many letters we shift each letter by. In our example we used an offset of 3, but could have also used 4 or 12.
如果只有发送方和接收方知道密钥，对称密钥密码术是很安全的。在凯撒密码中，**密钥是一个偏移值**，这个偏移值决定每个字母应该偏移多少。在我们的例子中，我们使用的偏移值是 3，但是也能是 4 或者 12。

The issue is that if Alice and Bob don’t meet before starting to send messages with the pigeon, they would have no way to establish a key securely. If they send the key in the message itself, Mallory would intercept the message and discover the key. This would allow Mallory to then read or change the message as she wishes before and after Alice and Bob start to encrypt their messages.
不过这么设计会有个问题：在用信鸽传递信息之前，如果 Alice 和 Bob 之前从没见过，他们没有安全的方式创建一个密钥。如果他们将密钥包含在信息之中，Mallory 将拦截信息并且发现密钥。后果就是：无论 Alice 和 Bob 发送的信息是否加密，Mallory 都能读取或者改变拦截到的信息。

This is the typical example of a **Man in the Middle Attack** and the only way to avoid it is to change the encryption system all together.

这是一个典型的**中间人攻击**例子。避免它的唯一方法是改变之前的密码系统。

## **Pigeons carrying boxes**
## **携带盒子的信鸽**
So Alice and Bob come up with an even better system. When Bob wants to send Alice a message 
she will follow the procedure below:
所以 Alice 和 Bob 想出了一个更好的系统。当 Bob 想要发送信息给 Alice 时，Alice 将遵照下面的流程：
- Bob sends a pigeon to Alice without any message.
- Alice sends the pigeon back carrying a box with an open lock, but keeping the key.
- Bob puts the message in the box, closes the locks and sends the box to Alice.
- Alice receives the box, opens it with the key and reads the message.
- Bob 向 Alice 传送一只信鸽，信鸽不携带任何信息。
- Alice 将这只信鸽传回给 Bob，信鸽携带一只开着锁的盒子以及密钥。
- Bob 把信息放到盒子里，将锁锁上，将盒子传送给 Alice。
- Alice 收到盒子，使用密钥打开盒子，读取信息。


This way Mallory can’t change the message by intercepting the pigeon, because she doesn’t have the key. The same process is followed when Alice wants to send Bob a message.

通过这种方式传递信息，Mallory 不可能通过拦截信鸽的方式来改变信息，因为她没有密钥。当 Alice 想要向 Bob 发送信息时，遵循相同的流程。

Alice and Bob just used what is commonly known as **asymmetric key cryptography**. It’s called asymmetric, because even if you can encrypt a message (lock the box) you can’t decrypt it (open a closed box).
In technical speech the box is known as the **public key** and the key to open it is known as the **private key**.

Alice 和 Bob 刚刚使用了通常所说的非对称密钥密码术。之所以称它为非对称，是因为即使你可以加密一条信息（锁上盒子）但你也不能将它解密（打开锁住的盒子）。

## **How do I trust the box?**
## **我怎么信任这个盒子？**
If you paid attention you may have noticed that we still have a problem. When Bob receives that open box how can he be sure that it came from Alice and that Mallory didn’t intercept the pigeon and changed the box with one she has the key to?

如果你够仔细的话，你可能已经意识到我们仍然有一个问题。当 Bob 收到那个开着的盒子时，他如何确信这是来自 Alice 的盒子，而不是 Mallory 拦截信鸽后，将来自于 Alice 的盒子替换成 Mallory 自己设置了密钥后的盒子。

Alice decides that she will sign the box, this way when Bob receives the box he checks the signature and knows that it was Alice who sent the box.

Alice 决定对盒子进行数字签名，通过这种方式，当 Bob 收到盒子，他通过核对签名的一致性来确定盒子是否来自 Alice。

Some of you may be thinking, how would Bob identify Alice’s signature in the first place? Good question. Alice and Bob had this problem too, so they decided that, instead of Alice signing the box, Ted will sign the box.

有些人可能就会想 Bob 如何识别 Alice 的签名？不错的问题。Alice 和 Bob 也有同样的疑问。因此他们决定让 Ted 对盒子进行数字签名，而不是 Alice。

Who is Ted? Ted is a very famous, well known and trustworthy guy. Ted gave his signature to everyone and everybody trusts that he will only sign boxes for legitimate people.

Ted 是谁？Ted 是一个著名且值得信赖的人。每个人都可以从Ted 那里获得签名，每个人都相信Ted 只会为合法的人提供盒子的数字签名服务。

Ted will only sign an Alice box if he’s sure that the one asking for the signature is Alice. So Mallory cannot get an Alice box signed by Ted on behalf of her as Bob will know that the box is a fraud because Ted only signs boxes for people after verifying their identity.

只有当Ted 确信正在请求签名的人是 Alice，Ted 才会为 Alice 提供盒子数字签名的服务。因此 Mallory 不能再像之前那样拦截 Alice 的盒子、替换盒子后传送给 Bob 了，因为 Bob 会发现这个盒子在 Ted 那进行数字签名的是    Mallory，而不是 Alice。

Ted in technical terms is commonly referred to as a **Certification Authority** and the browser you are reading this article with comes packaged with the signatures of various Certification Authorities.

Ted 在技术术语中通常被称为**证书颁发机构**，你阅读这篇文章所使用的浏览器安装着各种证书颁发机构的签名。

So when you connect to a website for the first time you trust its box because you trust Ted and Ted tells you that the box is legitimate.

因此当你第一次连接到一个网站，你信任它的盒子，因为你信任 Ted，而 Ted 告诉你这个盒子是合法的。

## **Boxes are heavy**
## **盒子太重了**
Alice and Bob now have a reliable system to communicate, but they realize that pigeons carrying boxes are slower than the ones carrying only the message.

Alice 和 Bob 现在有了一个可靠的通信系统，但是他们意识到和仅仅携带信息的信鸽相比，携带盒子的信鸽太慢了。

They decide that they will use the box method (asymmetric cryptography) only to choose a key to encrypt the message using symmetric cryptography with (remember the Caesar cipher?).

他们决定只在传递密钥的时候使用盒子的方法（非对称密码术），加密信息使用对称密码术（记得之前提到的凯撒密码？）。

This way they get the best of both worlds. The reliability of asymmetric cryptography and the efficiency of symmetric cryptography.

这样的话可谓两全其美：非对称密码术的可靠性和对称密码术的效率都有了。

In the real world there aren’t slow pigeons, but nonetheless encrypting messages using asymmetric cryptography is slower than using symmetric cryptography, so we only use it to exchange the encryption keys.

在现实世界中，“信鸽”的传送速度都很快，但尽管这么讲，使用非对称密码技术加密消息比使用对称密码技术慢，所以我们只使用它来交换加密密钥。

Now you know how **HTTPS** works and your coffee should also be ready. Go drink it you deserved it 😉

现在你知道了**HTTPS**的工作原理，你的咖啡也该煮好了。去喝吧，这是你应得的 😉
