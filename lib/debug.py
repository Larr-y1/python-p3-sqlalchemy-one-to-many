#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game, Review

if __name__ == '__main__':
    engine = create_engine('sqlite:///one_to_many.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    review = session.query(Review).first()
    review
    
    review.game_id
    
    session.query(Game).filter_by(id=review.game_id).first()

    review.game



    import ipdb; ipdb.set_trace()
