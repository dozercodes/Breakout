#!/usr/bin/python2.6

import main, gui, board, block, ball, paddle
import unittest

class MyTest(unittest.TestCase):
    def testMain(self):
        complete = main.main()
        self.assertTrue(complete)
    
    def testGUIStartGame(self):
        complete = gui.GUI.startGame(self)
        self.assertTrue(complete)
    
    def testGUIDrawBoard(self):
        complete = gui.GUI.drawBoard(self)
        self.assertTrue(complete)
    
    def testGUIDrawPaddle(self):
        complete = gui.GUI.drawPaddle(self)
        self.assertTrue(complete)
    
    def testGUIDrawBlocks(self):
        complete = gui.GUI.drawBlocks(self)
        self.assertTrue(complete)
    
    def testGUIDrawBall(self):
        complete = gui.GUI.drawBall(self)
        self.assertTrue(complete)
    
    def testBoardSetWidth(self):
        complete = board.Board.setWidth(self)
        self.assertTrue(complete)
    
    def testBoardSetHeight(self):
        complete = board.Board.setHeight(self)
        self.assertTrue(complete)
    
    def testBlockSetWidth(self):
        complete = block.Block.setWidth(self)
        self.assertTrue(complete)
    
    def testBlockSetHeight(self):
        complete = block.Block.setHeight(self)
        self.assertTrue(complete)
    
    def testBlockSetColor(self):
        complete = block.Block.setColor(self)
        self.assertTrue(complete)
    
    def testBlockOnHit(self):
        complete = block.Block.onHit(self)
        self.assertTrue(complete)
    
    def testBallSetDiameter(self):
        complete = ball.Ball.setDiameter(self)
        self.assertTrue(complete)
    
    def testBallSetSpeed(self):
        complete = ball.Ball.setSpeed(self)
        self.assertTrue(complete)
    
    def testBallMove(self):
        complete = ball.Ball.move(self)
        self.assertTrue(complete)
    
    def testPaddleSetWidth(self):
        complete = paddle.Paddle.setWidth(self)
        self.assertTrue(complete)
    
    def testPaddleSetHeight(self):
        complete = paddle.Paddle.setHeight(self)
        self.assertTrue(complete)
    
    def testPaddleMove(self):
        complete = paddle.Paddle.move(self)
        self.assertTrue(complete)   

if __name__ == '__main__':
    unittest.main()