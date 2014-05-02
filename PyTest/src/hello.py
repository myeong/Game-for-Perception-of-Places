#!/usr/bin/python27

import re
import textwrap


def clean_and_trim(string):
    if string:
        return string.replace('\n', ' ').strip()
    else:
        return None
    

target = """

                            <div id="HIST289C" class="course">
                                
                                <input type="hidden" name="courseId" value="HIST289C" />
                                
                                <div class="row">
                                    <div class="course-id-container one columns">
                                        
                                        <div class="course-id">HIST289C</div>
                                        
                                        
                                        
                                    </div>
                                    
                                    <div class="course-info-container eleven columns">
                                        
                                        <div class="course-basic-info-container sixteen colgrid">
                                            
                                            <div class="row">
                                                <div class="fifteen columns">
                                                    <span class="course-title">Mirror of Democracy: The Golden Age of Athens</span>
                                                </div>
                                                <div class="course-action-links-container one columns">
                                                    <a href="#" class="saved-course-section-toggle-link" title="Add to My Saved List">
                                                        <input type="hidden" name="courseId" value="HIST289C" />
                                                        <input type="hidden" name="sectionId" value="*" />
                                                        <img src="resources/images/unsaved-star.png" />
                                                    </a>
                                                </div>
                                            </div>
                                            
                                            <div class="course-stats-container row clearfix">
                                                
                                                <div class="course-credits-group two columns">
                                                    <div>
                                                        <span class="course-info-label">Credits:</span>
                                                        
                                                            
                                                                <span class="course-min-credits">3</span>
                                                            
                                                            
                                                        
                                                    </div>
                                                </div>
                                                
                                                <div class="grading-method-group five columns">
                                                    <div>
                                                        <span class="course-info-label"><abbr title="Grading Method"><span>Grad Meth</span></abbr></span>:
                                                        <span class="grading-method">
                                                            
                                                                
                                                                    <abbr title="Regular, Pass-Fail, Audit"><span>Reg, P-F, Aud</span></abbr>
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                            
                                                        </span>
                                                    </div>
                                                </div>
                                                
                                                <div class="core-codes-group two columns">
                                                    <div>
                                                        
                                                        
                                                        
                                                            
                                                            <span class="course-info-label">CORE:</span>
                                                            
                                                            
                                                                <a href="#" title="Social or Political History (SH)">SH</a>
                                                            
                                                            
                                                            
                                                            
                                                        
                                                        
                                                    </div>
                                                </div>
                                                
                                                <div class="gen-ed-codes-group six columns">
                                                    <div>
                                                        
                                                        
                                                        
                                                            
                                                            <span class="course-info-label"><abbr title="General Education"><span>GenEd</span></abbr></span>:
                                                            
                                                            
                                                            
                                                                
                                                                
                                                                
                                                                    <span class="course-subcategory">
                                                                        <a href="#" title="Distributive Studies - History and Social Sciences">DSHS</a></span>, 
                                                                
                                                            
                                                                
                                                                
                                                                
                                                                    <span class="course-subcategory">
                                                                        <a href="#" title="Signature Courses - I-Series">SCIS</a></span>
                                                                
                                                            
                                                            
                                                        
                                                        
                                                    </div>
                                                </div>
                                                
                                            </div>
                                            
                                        </div>
                                        
                                        
                                            
                                            <div class="approved-course-texts-container">
                                                
                                                
                                                
                                                
                                                
                                            </div>
                                            
                                        
                                        
                                        <div class="course-texts-container">
        
                                            
        
                                            
        
                                            
                                            
                                        </div>
                                        
                                        
                                        
                                            
                                            
                                            
                                            
                                                <div class="toggle-sections-link-container">
                                                    <div class="row">
                                                        <div class="sections-fieldset-container twelve columns">
                                                            <fieldset class="sections-fieldset sections-displayed">
                                                                <legend>
                                                                    
                                                                    
                                                                        
                                                                        
                                                                        
                                                                        
                                                                            <a href="#" class="toggle-sections-link"><span class="toggle-sections-arrow ui-icon ui-icon-triangle-1-s"></span><span class="toggle-sections-link-text">Hide Sections</span></a>
                                                                        
                                                                        
                                                                    
                                                                    
                                                                </legend>
                                                                
                                                                
                                                                
                                                                    
                                                                    


<div class="sections-container">
    
        
        
        
                
            <div class="sections sixteen colgrid">
                
                
                
                
                    <div class="section">
                        
                        <input type="hidden" name="sectionId" value="0101" />
                        
                        <div class="section-info-container">
                            <div class="row">
                                
                                
                                <div class="section-id-container two columns">
                                    
                                    <span class="section-id">
                                        0101
                                    </span>
                                    
                                    
                                    
                                </div>
                                
                                
                                <div class="section-instructors-container six columns">
                                    <span class="section-instructors">
                                        
                                        
                                            
                                            
                                                
                                                
                                                
                                                
                                                    
                                                    
                                                        
                                                            <span class="section-instructor">Kenneth Holum</span>
                                                        
                                                        
                                                    
                                                    
                                                
                                                
                                            
                                            
                                            
                                            
                                            
                                        
                                        
                                    </span>
                                </div>
                                
                                
                                <div class="seats-info-group six columns">
                                    <div>
                                        
                                        <span class="section-info-label">Seats</span>
                                        
                                        <span class="seats-info">
                                            
                                            <span class="total-seats">
                                                (<span class="seats-info-label">Total:</span>
                                                <span class="total-seats-count">25</span>,
                                            </span>
                                            
                                            <span class="open-seats ">
                                                <span class="seats-info-label">Open:</span>
                                                <span class="open-seats-count">0</span>,
                                            </span>
                                            
                                            <span class="waitlist ">
                                                <span class="seats-info-label">Waitlist:</span>
                                                <span class="waitlist-count">0</span>)
                                            </span>
                                            
                                        </span>
                                        
                                    </div>
                                </div>
                                
                                
                                <div class="section-action-links-container two columns">
                                    <!--
                                    <a href="#" class="saved-course-section-toggle-link" title="Add to My Saved List">
                                        <input type="hidden" name="courseId" value="HIST289C" />
                                        <input type="hidden" name="sectionId" value="0101" />
                                        <img src="resources/images/unsaved-star.png" />
                                    </a>
                                    -->
                                    <a href="#" class="bookstore-link">
                                        <img src="resources/images/bookstore.png" alt="Bookstore" title="Bookstore">
                                    </a>
                                </div>
                                
                            </div>
                        </div> <!-- end section-info-container -->
                        
                        
                        
                        <div class="class-days-container">
                            
                            
                                
                                
                                
                                
                                
                                    
                                        
                                        <div class="row">
                                            
                                            
                                                
                                                
                                                
                                                
                                                
                                                
                                                    
                                                    
                                                    <div class="section-day-time-group push_two five columns">
                                                        
                                                        
                                                            
                                                            
                                                                <span class="section-days">TuTh</span>
                                                                <span class="class-start-time">11:00am</span> - <span class="class-end-time">11:50am</span>
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                        
                                                        
                                                    </div>
                                                    
                                                    
                                                    <div class="section-class-building-group push_one three columns">
                                                        
                                                        <span class="class-building">
                                                            
                                                            
                                                                
                                                                
                                                                
                                                                    <a href="http://www.umd.edu/CampusMaps/bld_detail.cfm?bld_code=KEY" target="_blank"><span class="building-code">KEY</span></a>
                                                                    <span class="class-room">0102</span>
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                            
                                                            
                                                        </span>
                                                        
                                                    </div>
                                                    
                                                
                                                
                                            
                                            
                                            
                                            
                                                
                                                
                                            
                                            
                                        </div> 
                                        
                                    
                                        
                                        <div class="row">
                                            
                                            
                                                
                                                
                                                
                                                
                                                
                                                
                                                    
                                                    
                                                    <div class="section-day-time-group push_two five columns">
                                                        
                                                        
                                                            
                                                            
                                                                <span class="section-days">Tu</span>
                                                                <span class="class-start-time">9:30am</span> - <span class="class-end-time">10:20am</span>
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                        
                                                        
                                                    </div>
                                                    
                                                    
                                                    <div class="section-class-building-group push_one three columns">
                                                        
                                                        <span class="class-building">
                                                            
                                                            
                                                                
                                                                
                                                                
                                                                    <a href="http://www.umd.edu/CampusMaps/bld_detail.cfm?bld_code=SQH" target="_blank"><span class="building-code">SQH</span></a>
                                                                    <span class="class-room">1101</span>
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                            
                                                            
                                                        </span>
                                                        
                                                    </div>
                                                    
                                                
                                                
                                            
                                            
                                            
                                            
                                                
                                                
                                                    <div class="two columns">
                                                        <span class="class-type">Discussion</span>
                                                    </div>
                                                
                                            
                                            
                                        </div> 
                                        
                                     
                                
                                
                            
                            
                        </div> 
                        
                        
                        
                    </div> 
                
                    <div class="section">
                        
                        <input type="hidden" name="sectionId" value="0102" />
                        
                        <div class="section-info-container">
                            <div class="row">
                                
                                
                                <div class="section-id-container two columns">
                                    
                                    <span class="section-id">
                                        0102
                                    </span>
                                    
                                    
                                    
                                </div>
                                
                                
                                <div class="section-instructors-container six columns">
                                    <span class="section-instructors">
                                        
                                        
                                            
                                            
                                                
                                                
                                                
                                                
                                                    
                                                    
                                                        
                                                            <span class="section-instructor">Kenneth Holum</span>
                                                        
                                                        
                                                    
                                                    
                                                
                                                
                                            
                                            
                                            
                                            
                                            
                                        
                                        
                                    </span>
                                </div>
                                
                                
                                <div class="seats-info-group six columns">
                                    <div>
                                        
                                        <span class="section-info-label">Seats</span>
                                        
                                        <span class="seats-info">
                                            
                                            <span class="total-seats">
                                                (<span class="seats-info-label">Total:</span>
                                                <span class="total-seats-count">25</span>,
                                            </span>
                                            
                                            <span class="open-seats has-open-seats">
                                                <span class="seats-info-label">Open:</span>
                                                <span class="open-seats-count">2</span>,
                                            </span>
                                            
                                            <span class="waitlist ">
                                                <span class="seats-info-label">Waitlist:</span>
                                                <span class="waitlist-count">0</span>)
                                            </span>
                                            
                                        </span>
                                        
                                    </div>
                                </div>
                                
                                
                                <div class="section-action-links-container two columns">
                                    <!--
                                    <a href="#" class="saved-course-section-toggle-link" title="Add to My Saved List">
                                        <input type="hidden" name="courseId" value="HIST289C" />
                                        <input type="hidden" name="sectionId" value="0102" />
                                        <img src="resources/images/unsaved-star.png" />
                                    </a>
                                    -->
                                    <a href="#" class="bookstore-link">
                                        <img src="resources/images/bookstore.png" alt="Bookstore" title="Bookstore">
                                    </a>
                                </div>
                                
                            </div>
                        </div> <!-- end section-info-container -->
                        
                        
                        
                        <div class="class-days-container">
                            
                            
                                
                                
                                
                                
                                
                                    
                                        
                                        <div class="row">
                                            
                                            
                                                
                                                
                                                
                                                
                                                
                                                
                                                    
                                                    
                                                    <div class="section-day-time-group push_two five columns">
                                                        
                                                        
                                                            
                                                            
                                                                <span class="section-days">TuTh</span>
                                                                <span class="class-start-time">11:00am</span> - <span class="class-end-time">11:50am</span>
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                        
                                                        
                                                    </div>
                                                    
                                                    
                                                    <div class="section-class-building-group push_one three columns">
                                                        
                                                        <span class="class-building">
                                                            
                                                            
                                                                
                                                                
                                                                
                                                                    <a href="http://www.umd.edu/CampusMaps/bld_detail.cfm?bld_code=KEY" target="_blank"><span class="building-code">KEY</span></a>
                                                                    <span class="class-room">0102</span>
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                            
                                                            
                                                        </span>
                                                        
                                                    </div>
                                                    
                                                
                                                
                                            
                                            
                                            
                                            
                                                
                                                
                                            
                                            
                                        </div> 
                                        
                                    
                                        
                                        <div class="row">
                                            
                                            
                                                
                                                
                                                
                                                
                                                
                                                
                                                    
                                                    
                                                    <div class="section-day-time-group push_two five columns">
                                                        
                                                        
                                                            
                                                            
                                                                <span class="section-days">Tu</span>
                                                                <span class="class-start-time">12:30pm</span> - <span class="class-end-time">1:20pm</span>
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                        
                                                        
                                                    </div>
                                                    
                                                    
                                                    <div class="section-class-building-group push_one three columns">
                                                        
                                                        <span class="class-building">
                                                            
                                                            
                                                                
                                                                
                                                                
                                                                    <a href="http://www.umd.edu/CampusMaps/bld_detail.cfm?bld_code=EDU" target="_blank"><span class="building-code">EDU</span></a>
                                                                    <span class="class-room">2101</span>
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                            
                                                            
                                                        </span>
                                                        
                                                    </div>
                                                    
                                                
                                                
                                            
                                            
                                            
                                            
                                                
                                                
                                                    <div class="two columns">
                                                        <span class="class-type">Discussion</span>
                                                    </div>
                                                
                                            
                                            
                                        </div> 
                                        
                                     
                                
                                
                            
                            
                        </div> 
                        
                        
                        
                    </div> 
                
                    <div class="section">
                        
                        <input type="hidden" name="sectionId" value="0103" />
                        
                        <div class="section-info-container">
                            <div class="row">
                                
                                
                                <div class="section-id-container two columns">
                                    
                                    <span class="section-id">
                                        0103
                                    </span>
                                    
                                    
                                    
                                </div>
                                
                                
                                <div class="section-instructors-container six columns">
                                    <span class="section-instructors">
                                        
                                        
                                            
                                            
                                                
                                                
                                                
                                                
                                                    
                                                    
                                                        
                                                            <span class="section-instructor">Kenneth Holum</span>
                                                        
                                                        
                                                    
                                                    
                                                
                                                
                                            
                                            
                                            
                                            
                                            
                                        
                                        
                                    </span>
                                </div>
                                
                                
                                <div class="seats-info-group six columns">
                                    <div>
                                        
                                        <span class="section-info-label">Seats</span>
                                        
                                        <span class="seats-info">
                                            
                                            <span class="total-seats">
                                                (<span class="seats-info-label">Total:</span>
                                                <span class="total-seats-count">25</span>,
                                            </span>
                                            
                                            <span class="open-seats has-open-seats">
                                                <span class="seats-info-label">Open:</span>
                                                <span class="open-seats-count">1</span>,
                                            </span>
                                            
                                            <span class="waitlist ">
                                                <span class="seats-info-label">Waitlist:</span>
                                                <span class="waitlist-count">0</span>)
                                            </span>
                                            
                                        </span>
                                        
                                    </div>
                                </div>
                                
                                
                                <div class="section-action-links-container two columns">
                                    <!--
                                    <a href="#" class="saved-course-section-toggle-link" title="Add to My Saved List">
                                        <input type="hidden" name="courseId" value="HIST289C" />
                                        <input type="hidden" name="sectionId" value="0103" />
                                        <img src="resources/images/unsaved-star.png" />
                                    </a>
                                    -->
                                    <a href="#" class="bookstore-link">
                                        <img src="resources/images/bookstore.png" alt="Bookstore" title="Bookstore">
                                    </a>
                                </div>
                                
                            </div>
                        </div> <!-- end section-info-container -->
                        
                        
                        
                        <div class="class-days-container">
                            
                            
                                
                                
                                
                                
                                
                                    
                                        
                                        <div class="row">
                                            
                                            
                                                
                                                
                                                
                                                
                                                
                                                
                                                    
                                                    
                                                    <div class="section-day-time-group push_two five columns">
                                                        
                                                        
                                                            
                                                            
                                                                <span class="section-days">TuTh</span>
                                                                <span class="class-start-time">11:00am</span> - <span class="class-end-time">11:50am</span>
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                        
                                                        
                                                    </div>
                                                    
                                                    
                                                    <div class="section-class-building-group push_one three columns">
                                                        
                                                        <span class="class-building">
                                                            
                                                            
                                                                
                                                                
                                                                
                                                                    <a href="http://www.umd.edu/CampusMaps/bld_detail.cfm?bld_code=KEY" target="_blank"><span class="building-code">KEY</span></a>
                                                                    <span class="class-room">0102</span>
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                            
                                                            
                                                        </span>
                                                        
                                                    </div>
                                                    
                                                
                                                
                                            
                                            
                                            
                                            
                                                
                                                
                                            
                                            
                                        </div> 
                                        
                                    
                                        
                                        <div class="row">
                                            
                                            
                                                
                                                
                                                
                                                
                                                
                                                
                                                    
                                                    
                                                    <div class="section-day-time-group push_two five columns">
                                                        
                                                        
                                                            
                                                            
                                                                <span class="section-days">Th</span>
                                                                <span class="class-start-time">9:30am</span> - <span class="class-end-time">10:20am</span>
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                        
                                                        
                                                    </div>
                                                    
                                                    
                                                    <div class="section-class-building-group push_one three columns">
                                                        
                                                        <span class="class-building">
                                                            
                                                            
                                                                
                                                                
                                                                
                                                                    <a href="http://www.umd.edu/CampusMaps/bld_detail.cfm?bld_code=EDU" target="_blank"><span class="building-code">EDU</span></a>
                                                                    <span class="class-room">2119</span>
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                            
                                                            
                                                        </span>
                                                        
                                                    </div>
                                                    
                                                
                                                
                                            
                                            
                                            
                                            
                                                
                                                
                                                    <div class="two columns">
                                                        <span class="class-type">Discussion</span>
                                                    </div>
                                                
                                            
                                            
                                        </div> 
                                        
                                     
                                
                                
                            
                            
                        </div> 
                        
                        
                        
                    </div> 
                 
                
            </div>
            
            
            
            
        
        
        
        
        
    
</div>

                                                                
                                                                
                                                            </fieldset>
                                                        </div>
                                                    </div>
                                                </div>
                                            
                                            
                                        
                                        
                                    </div>
                                </div>
                                
                            </div> 
                            
                        
                            
                            
                            
                            
                            <div id="HIST289R" class="course">
                                
                                <input type="hidden" name="courseId" value="HIST289R" />
                                
                                <div class="row">
                                    <div class="course-id-container one columns">
                                        
                                        <div class="course-id">HIST289R</div>
                                        
                                        
                                        
                                    </div>
                                    
                                    <div class="course-info-container eleven columns">
                                        
                                        <div class="course-basic-info-container sixteen colgrid">
                                            
                                            <div class="row">
                                                <div class="fifteen columns">
                                                    <span class="course-title">Pocketbook Politics: A History of American Buying and Selling</span>
                                                </div>
                                                <div class="course-action-links-container one columns">
                                                    <a href="#" class="saved-course-section-toggle-link" title="Add to My Saved List">
                                                        <input type="hidden" name="courseId" value="HIST289R" />
                                                        <input type="hidden" name="sectionId" value="*" />
                                                        <img src="resources/images/unsaved-star.png" />
                                                    </a>
                                                </div>
                                            </div>
                                            
                                            <div class="course-stats-container row clearfix">
                                                
                                                <div class="course-credits-group two columns">
                                                    <div>
                                                        <span class="course-info-label">Credits:</span>
                                                        
                                                            
                                                                <span class="course-min-credits">3</span>
                                                            
                                                            
                                                        
                                                    </div>
                                                </div>
                                                
                                                <div class="grading-method-group five columns">
                                                    <div>
                                                        <span class="course-info-label"><abbr title="Grading Method"><span>Grad Meth</span></abbr></span>:
                                                        <span class="grading-method">
                                                            
                                                                
                                                                    <abbr title="Regular, Pass-Fail, Audit"><span>Reg, P-F, Aud</span></abbr>
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                            
                                                        </span>
                                                    </div>
                                                </div>
                                                
                                                <div class="core-codes-group two columns">
                                                    <div>
                                                        
                                                        
                                                        
                                                        
                                                    </div>
                                                </div>
                                                
                                                <div class="gen-ed-codes-group six columns">
                                                    <div>
                                                        
                                                        
                                                        
                                                            
                                                            <span class="course-info-label"><abbr title="General Education"><span>GenEd</span></abbr></span>:
                                                            
                                                            
                                                            
                                                                
                                                                
                                                                
                                                                    <span class="course-subcategory">
                                                                        <a href="#" title="Distributive Studies - Humanities">DSHU</a></span>, 
                                                                
                                                            
                                                                
                                                                
                                                                
                                                                    <span class="course-subcategory">
                                                                        <a href="#" title="Signature Courses - I-Series">SCIS</a></span>
                                                                
                                                            
                                                            
                                                        
                                                        
                                                    </div>
                                                </div>
                                                
                                            </div>
                                            
                                        </div>
                                        
                                        
                                            
                                            <div class="approved-course-texts-container">
                                                
                                                
                                                
                                                
                                                
                                            </div>
                                            
                                        
                                        
                                        <div class="course-texts-container">
        
                                            
                                                <div class="row">
                                                    <div class="twelve columns">
                                                        <div class="course-text">This course is designed to provide a thematic approach to consumer culture as it emerged in the United States over the course of three centuries. Drawing on history, anthropology, sociology, and media/communication studies, this course will examine the key moments in American consumer history and the major debates in the meanings of consumption. Consumerism has been described as the basis of widespread prosperity and social equality, the enemy of moral values, and a basic right of citizenship. The history of consumption is a prism through which many aspects of social and political life may be viewed. How does what we wear, what we listen to, or what we eat shape our identities?</div>
                                                    </div>
                                                </div>
                                            
        
                                            
        
                                            
                                            
                                        </div>
                                        
                                        
                                        
                                            
                                            
                                            
                                            
                                                <div class="toggle-sections-link-container">
                                                    <div class="row">
                                                        <div class="sections-fieldset-container twelve columns">
                                                            <fieldset class="sections-fieldset sections-displayed">
                                                                <legend>
                                                                    
                                                                    
                                                                        
                                                                        
                                                                        
                                                                        
                                                                            <a href="#" class="toggle-sections-link"><span class="toggle-sections-arrow ui-icon ui-icon-triangle-1-s"></span><span class="toggle-sections-link-text">Hide Sections</span></a>
                                                                        
                                                                        
                                                                    
                                                                    
                                                                </legend>
                                                                
                                                                
                                                                
                                                                    
                                                                    


<div class="sections-container">
    
        
        
        
                
            <div class="sections sixteen colgrid">
                
                
                
                
                    <div class="section">
                        
                        <input type="hidden" name="sectionId" value="0101" />
                        
                        <div class="section-info-container">
                            <div class="row">
                                
                                
                                <div class="section-id-container two columns">
                                    
                                    <span class="section-id">
                                        0101
                                    </span>
                                    
                                    
                                    
                                </div>
                                
                                
                                <div class="section-instructors-container six columns">
                                    <span class="section-instructors">
                                        
                                        
                                            
                                            
                                                
                                                
                                                
                                                
                                                    
                                                    
                                                        
                                                            <span class="section-instructor">Katarina Keane</span>
                                                        
                                                        
                                                    
                                                    
                                                
                                                
                                            
                                            
                                            
                                            
                                            
                                        
                                        
                                    </span>
                                </div>
                                
                                
                                <div class="seats-info-group six columns">
                                    <div>
                                        
                                        <span class="section-info-label">Seats</span>
                                        
                                        <span class="seats-info">
                                            
                                            <span class="total-seats">
                                                (<span class="seats-info-label">Total:</span>
                                                <span class="total-seats-count">20</span>,
                                            </span>
                                            
                                            <span class="open-seats has-open-seats">
                                                <span class="seats-info-label">Open:</span>
                                                <span class="open-seats-count">1</span>,
                                            </span>
                                            
                                            <span class="waitlist ">
                                                <span class="seats-info-label">Waitlist:</span>
                                                <span class="waitlist-count">0</span>)
                                            </span>
                                            
                                        </span>
                                        
                                    </div>
                                </div>
                                
                                
                                <div class="section-action-links-container two columns">
                                    <!--
                                    <a href="#" class="saved-course-section-toggle-link" title="Add to My Saved List">
                                        <input type="hidden" name="courseId" value="HIST289R" />
                                        <input type="hidden" name="sectionId" value="0101" />
                                        <img src="resources/images/unsaved-star.png" />
                                    </a>
                                    -->
                                    <a href="#" class="bookstore-link">
                                        <img src="resources/images/bookstore.png" alt="Bookstore" title="Bookstore">
                                    </a>
                                </div>
                                
                            </div>
                        </div> <!-- end section-info-container -->
                        
                        
                        
                        <div class="class-days-container">
                            
                            
                                
                                
                                
                                
                                
                                    
                                        
                                        <div class="row">
                                            
                                            
                                                
                                                
                                                
                                                
                                                
                                                
                                                    
                                                    
                                                    <div class="section-day-time-group push_two five columns">
                                                        
                                                        
                                                            
                                                            
                                                                <span class="section-days">TuTh</span>
                                                                <span class="class-start-time">9:30am</span> - <span class="class-end-time">10:20am</span>
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                        
                                                        
                                                    </div>
                                                    
                                                    
                                                    <div class="section-class-building-group push_one three columns">
                                                        
                                                        <span class="class-building">
                                                            
                                                            
                                                                
                                                                
                                                                
                                                                    <a href="http://www.umd.edu/CampusMaps/bld_detail.cfm?bld_code=MMH" target="_blank"><span class="building-code">MMH</span></a>
                                                                    <span class="class-room">1400</span>
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                            
                                                            
                                                        </span>
                                                        
                                                    </div>
                                                    
                                                
                                                
                                            
                                            
                                            
                                            
                                                
                                                
                                            
                                            
                                        </div> 
                                        
                                    
                                        
                                        <div class="row">
                                            
                                            
                                                
                                                
                                                
                                                
                                                
                                                
                                                    
                                                    
                                                    <div class="section-day-time-group push_two five columns">
                                                        
                                                        
                                                            
                                                            
                                                                <span class="section-days">Tu</span>
                                                                <span class="class-start-time">11:00am</span> - <span class="class-end-time">11:50am</span>
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                        
                                                        
                                                    </div>
                                                    
                                                    
                                                    <div class="section-class-building-group push_one three columns">
                                                        
                                                        <span class="class-building">
                                                            
                                                            
                                                                
                                                                
                                                                
                                                                    <a href="http://www.umd.edu/CampusMaps/bld_detail.cfm?bld_code=KEY" target="_blank"><span class="building-code">KEY</span></a>
                                                                    <span class="class-room">0123</span>
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                            
                                                            
                                                        </span>
                                                        
                                                    </div>
                                                    
                                                
                                                
                                            
                                            
                                            
                                            
                                                
                                                
                                                    <div class="two columns">
                                                        <span class="class-type">Discussion</span>
                                                    </div>
                                                
                                            
                                            
                                        </div> 
                                        
                                     
                                
                                
                            
                            
                        </div> 
                        
                        
                        
                    </div> 
                
                    <div class="section">
                        
                        <input type="hidden" name="sectionId" value="0102" />
                        
                        <div class="section-info-container">
                            <div class="row">
                                
                                
                                <div class="section-id-container two columns">
                                    
                                    <span class="section-id">
                                        0102
                                    </span>
                                    
                                    
                                    
                                </div>
                                
                                
                                <div class="section-instructors-container six columns">
                                    <span class="section-instructors">
                                        
                                        
                                            
                                            
                                                
                                                
                                                
                                                
                                                    
                                                    
                                                        
                                                            <span class="section-instructor">Katarina Keane</span>
                                                        
                                                        
                                                    
                                                    
                                                
                                                
                                            
                                            
                                            
                                            
                                            
                                        
                                        
                                    </span>
                                </div>
                                
                                
                                <div class="seats-info-group six columns">
                                    <div>
                                        
                                        <span class="section-info-label">Seats</span>
                                        
                                        <span class="seats-info">
                                            
                                            <span class="total-seats">
                                                (<span class="seats-info-label">Total:</span>
                                                <span class="total-seats-count">20</span>,
                                            </span>
                                            
                                            <span class="open-seats ">
                                                <span class="seats-info-label">Open:</span>
                                                <span class="open-seats-count">0</span>,
                                            </span>
                                            
                                            <span class="waitlist ">
                                                <span class="seats-info-label">Waitlist:</span>
                                                <span class="waitlist-count">0</span>)
                                            </span>
                                            
                                        </span>
                                        
                                    </div>
                                </div>
                                
                                
                                <div class="section-action-links-container two columns">
                                    <!--
                                    <a href="#" class="saved-course-section-toggle-link" title="Add to My Saved List">
                                        <input type="hidden" name="courseId" value="HIST289R" />
                                        <input type="hidden" name="sectionId" value="0102" />
                                        <img src="resources/images/unsaved-star.png" />
                                    </a>
                                    -->
                                    <a href="#" class="bookstore-link">
                                        <img src="resources/images/bookstore.png" alt="Bookstore" title="Bookstore">
                                    </a>
                                </div>
                                
                            </div>
                        </div> <!-- end section-info-container -->
                        
                        
                        
                        <div class="class-days-container">
                            
                            
                                
                                
                                
                                
                                
                                    
                                        
                                        <div class="row">
                                            
                                            
                                                
                                                
                                                
                                                
                                                
                                                
                                                    
                                                    
                                                    <div class="section-day-time-group push_two five columns">
                                                        
                                                        
                                                            
                                                            
                                                                <span class="section-days">TuTh</span>
                                                                <span class="class-start-time">9:30am</span> - <span class="class-end-time">10:20am</span>
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                        
                                                        
                                                    </div>
                                                    
                                                    
                                                    <div class="section-class-building-group push_one three columns">
                                                        
                                                        <span class="class-building">
                                                            
                                                            
                                                                
                                                                
                                                                
                                                                    <a href="http://www.umd.edu/CampusMaps/bld_detail.cfm?bld_code=MMH" target="_blank"><span class="building-code">MMH</span></a>
                                                                    <span class="class-room">1400</span>
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                            
                                                            
                                                        </span>
                                                        
                                                    </div>
                                                    
                                                
                                                
                                            
                                            
                                            
                                            
                                                
                                                
                                            
                                            
                                        </div> 
                                        
                                    
                                        
                                        <div class="row">
                                            
                                            
                                                
                                                
                                                
                                                
                                                
                                                
                                                    
                                                    
                                                    <div class="section-day-time-group push_two five columns">
                                                        
                                                        
                                                            
                                                            
                                                                <span class="section-days">Tu</span>
                                                                <span class="class-start-time">12:30pm</span> - <span class="class-end-time">1:20pm</span>
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                        
                                                        
                                                    </div>
                                                    
                                                    
                                                    <div class="section-class-building-group push_one three columns">
                                                        
                                                        <span class="class-building">
                                                            
                                                            
                                                                
                                                                
                                                                
                                                                    <a href="http://www.umd.edu/CampusMaps/bld_detail.cfm?bld_code=KEY" target="_blank"><span class="building-code">KEY</span></a>
                                                                    <span class="class-room">0124</span>
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                            
                                                            
                                                        </span>
                                                        
                                                    </div>
                                                    
                                                
                                                
                                            
                                            
                                            
                                            
                                                
                                                
                                                    <div class="two columns">
                                                        <span class="class-type">Discussion</span>
                                                    </div>
                                                
                                            
                                            
                                        </div> 
                                        
                                     
                                
                                
                            
                            
                        </div> 
                        
                        
                        
                    </div> 
                
                    <div class="section">
                        
                        <input type="hidden" name="sectionId" value="0103" />
                        
                        <div class="section-info-container">
                            <div class="row">
                                
                                
                                <div class="section-id-container two columns">
                                    
                                    <span class="section-id">
                                        0103
                                    </span>
                                    
                                    
                                    
                                </div>
                                
                                
                                <div class="section-instructors-container six columns">
                                    <span class="section-instructors">
                                        
                                        
                                            
                                            
                                                
                                                
                                                
                                                
                                                    
                                                    
                                                        
                                                            <span class="section-instructor">Katarina Keane</span>
                                                        
                                                        
                                                    
                                                    
                                                
                                                
                                            
                                            
                                            
                                            
                                            
                                        
                                        
                                    </span>
                                </div>
                                
                                
                                <div class="seats-info-group six columns">
                                    <div>
                                        
                                        <span class="section-info-label">Seats</span>
                                        
                                        <span class="seats-info">
                                            
                                            <span class="total-seats">
                                                (<span class="seats-info-label">Total:</span>
                                                <span class="total-seats-count">20</span>,
                                            </span>
                                            
                                            <span class="open-seats ">
                                                <span class="seats-info-label">Open:</span>
                                                <span class="open-seats-count">0</span>,
                                            </span>
                                            
                                            <span class="waitlist ">
                                                <span class="seats-info-label">Waitlist:</span>
                                                <span class="waitlist-count">0</span>)
                                            </span>
                                            
                                        </span>
                                        
                                    </div>
                                </div>
                                
                                
                                <div class="section-action-links-container two columns">
                                    <!--
                                    <a href="#" class="saved-course-section-toggle-link" title="Add to My Saved List">
                                        <input type="hidden" name="courseId" value="HIST289R" />
                                        <input type="hidden" name="sectionId" value="0103" />
                                        <img src="resources/images/unsaved-star.png" />
                                    </a>
                                    -->
                                    <a href="#" class="bookstore-link">
                                        <img src="resources/images/bookstore.png" alt="Bookstore" title="Bookstore">
                                    </a>
                                </div>
                                
                            </div>
                        </div> <!-- end section-info-container -->
                        
                        
                        
                        <div class="class-days-container">
                            
                            
                                
                                
                                
                                
                                
                                    
                                        
                                        <div class="row">
                                            
                                            
                                                
                                                
                                                
                                                
                                                
                                                
                                                    
                                                    
                                                    <div class="section-day-time-group push_two five columns">
                                                        
                                                        
                                                            
                                                            
                                                                <span class="section-days">TuTh</span>
                                                                <span class="class-start-time">9:30am</span> - <span class="class-end-time">10:20am</span>
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                        
                                                        
                                                    </div>
                                                    
                                                    
                                                    <div class="section-class-building-group push_one three columns">
                                                        
                                                        <span class="class-building">
                                                            
                                                            
                                                                
                                                                
                                                                
                                                                    <a href="http://www.umd.edu/CampusMaps/bld_detail.cfm?bld_code=MMH" target="_blank"><span class="building-code">MMH</span></a>
                                                                    <span class="class-room">1400</span>
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                            
                                                            
                                                        </span>
                                                        
                                                    </div>
                                                    
                                                
                                                
                                            
                                            
                                            
                                            
                                                
                                                
                                            
                                            
                                        </div> 
                                        
                                    
                                        
                                        <div class="row">
                                            
                                            
                                                
                                                
                                                
                                                
                                                
                                                
                                                    
                                                    
                                                    <div class="section-day-time-group push_two five columns">
                                                        
                                                        
                                                            
                                                            
                                                                <span class="section-days">Th</span>
                                                                <span class="class-start-time">11:00am</span> - <span class="class-end-time">11:50am</span>
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                        
                                                        
                                                    </div>
                                                    
                                                    
                                                    <div class="section-class-building-group push_one three columns">
                                                        
                                                        <span class="class-building">
                                                            
                                                            
                                                                
                                                                
                                                                
                                                                    <a href="http://www.umd.edu/CampusMaps/bld_detail.cfm?bld_code=TLF" target="_blank"><span class="building-code">TLF</span></a>
                                                                    <span class="class-room">1101</span>
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                            
                                                            
                                                        </span>
                                                        
                                                    </div>
                                                    
                                                
                                                
                                            
                                            
                                            
                                            
                                                
                                                
                                                    <div class="two columns">
                                                        <span class="class-type">Discussion</span>
                                                    </div>
                                                
                                            
                                            
                                        </div> 
                                        
                                     
                                
                                
                            
                            
                        </div> 
                        
                        
                        
                    </div> 
                
                    <div class="section">
                        
                        <input type="hidden" name="sectionId" value="0104" />
                        
                        <div class="section-info-container">
                            <div class="row">
                                
                                
                                <div class="section-id-container two columns">
                                    
                                    <span class="section-id">
                                        0104
                                    </span>
                                    
                                    
                                    
                                </div>
                                
                                
                                <div class="section-instructors-container six columns">
                                    <span class="section-instructors">
                                        
                                        
                                            
                                            
                                                
                                                
                                                
                                                
                                                    
                                                    
                                                        
                                                            <span class="section-instructor">Katarina Keane</span>
                                                        
                                                        
                                                    
                                                    
                                                
                                                
                                            
                                            
                                            
                                            
                                            
                                        
                                        
                                    </span>
                                </div>
                                
                                
                                <div class="seats-info-group six columns">
                                    <div>
                                        
                                        <span class="section-info-label">Seats</span>
                                        
                                        <span class="seats-info">
                                            
                                            <span class="total-seats">
                                                (<span class="seats-info-label">Total:</span>
                                                <span class="total-seats-count">20</span>,
                                            </span>
                                            
                                            <span class="open-seats ">
                                                <span class="seats-info-label">Open:</span>
                                                <span class="open-seats-count">0</span>,
                                            </span>
                                            
                                            <span class="waitlist ">
                                                <span class="seats-info-label">Waitlist:</span>
                                                <span class="waitlist-count">0</span>)
                                            </span>
                                            
                                        </span>
                                        
                                    </div>
                                </div>
                                
                                
                                <div class="section-action-links-container two columns">
                                    <!--
                                    <a href="#" class="saved-course-section-toggle-link" title="Add to My Saved List">
                                        <input type="hidden" name="courseId" value="HIST289R" />
                                        <input type="hidden" name="sectionId" value="0104" />
                                        <img src="resources/images/unsaved-star.png" />
                                    </a>
                                    -->
                                    <a href="#" class="bookstore-link">
                                        <img src="resources/images/bookstore.png" alt="Bookstore" title="Bookstore">
                                    </a>
                                </div>
                                
                            </div>
                        </div> <!-- end section-info-container -->
                        
                        
                        
                        <div class="class-days-container">
                            
                            
                                
                                
                                
                                
                                
                                    
                                        
                                        <div class="row">
                                            
                                            
                                                
                                                
                                                
                                                
                                                
                                                
                                                    
                                                    
                                                    <div class="section-day-time-group push_two five columns">
                                                        
                                                        
                                                            
                                                            
                                                                <span class="section-days">TuTh</span>
                                                                <span class="class-start-time">9:30am</span> - <span class="class-end-time">10:20am</span>
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                        
                                                        
                                                    </div>
                                                    
                                                    
                                                    <div class="section-class-building-group push_one three columns">
                                                        
                                                        <span class="class-building">
                                                            
                                                            
                                                                
                                                                
                                                                
                                                                    <a href="http://www.umd.edu/CampusMaps/bld_detail.cfm?bld_code=MMH" target="_blank"><span class="building-code">MMH</span></a>
                                                                    <span class="class-room">1400</span>
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                            
                                                            
                                                        </span>
                                                        
                                                    </div>
                                                    
                                                
                                                
                                            
                                            
                                            
                                            
                                                
                                                
                                            
                                            
                                        </div> 
                                        
                                    
                                        
                                        <div class="row">
                                            
                                            
                                                
                                                
                                                
                                                
                                                
                                                
                                                    
                                                    
                                                    <div class="section-day-time-group push_two five columns">
                                                        
                                                        
                                                            
                                                            
                                                                <span class="section-days">F</span>
                                                                <span class="class-start-time">9:00am</span> - <span class="class-end-time">9:50am</span>
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                        
                                                        
                                                    </div>
                                                    
                                                    
                                                    <div class="section-class-building-group push_one three columns">
                                                        
                                                        <span class="class-building">
                                                            
                                                            
                                                                
                                                                
                                                                
                                                                    <a href="http://www.umd.edu/CampusMaps/bld_detail.cfm?bld_code=WDS" target="_blank"><span class="building-code">WDS</span></a>
                                                                    <span class="class-room">1130</span>
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                            
                                                            
                                                        </span>
                                                        
                                                    </div>
                                                    
                                                
                                                
                                            
                                            
                                            
                                            
                                                
                                                
                                                    <div class="two columns">
                                                        <span class="class-type">Discussion</span>
                                                    </div>
                                                
                                            
                                            
                                        </div> 
                                        
                                     
                                
                                
                            
                            
                        </div> 
                        
                        
                        
                    </div> 
                
                    <div class="section">
                        
                        <input type="hidden" name="sectionId" value="0105" />
                        
                        <div class="section-info-container">
                            <div class="row">
                                
                                
                                <div class="section-id-container two columns">
                                    
                                    <span class="section-id">
                                        0105
                                    </span>
                                    
                                    
                                    
                                </div>
                                
                                
                                <div class="section-instructors-container six columns">
                                    <span class="section-instructors">
                                        
                                        
                                            
                                            
                                                
                                                
                                                
                                                
                                                    
                                                    
                                                        
                                                            <span class="section-instructor">Katarina Keane</span>
                                                        
                                                        
                                                    
                                                    
                                                
                                                
                                            
                                            
                                            
                                            
                                            
                                        
                                        
                                    </span>
                                </div>
                                
                                
                                <div class="seats-info-group six columns">
                                    <div>
                                        
                                        <span class="section-info-label">Seats</span>
                                        
                                        <span class="seats-info">
                                            
                                            <span class="total-seats">
                                                (<span class="seats-info-label">Total:</span>
                                                <span class="total-seats-count">20</span>,
                                            </span>
                                            
                                            <span class="open-seats ">
                                                <span class="seats-info-label">Open:</span>
                                                <span class="open-seats-count">0</span>,
                                            </span>
                                            
                                            <span class="waitlist ">
                                                <span class="seats-info-label">Waitlist:</span>
                                                <span class="waitlist-count">0</span>)
                                            </span>
                                            
                                        </span>
                                        
                                    </div>
                                </div>
                                
                                
                                <div class="section-action-links-container two columns">
                                    <!--
                                    <a href="#" class="saved-course-section-toggle-link" title="Add to My Saved List">
                                        <input type="hidden" name="courseId" value="HIST289R" />
                                        <input type="hidden" name="sectionId" value="0105" />
                                        <img src="resources/images/unsaved-star.png" />
                                    </a>
                                    -->
                                    <a href="#" class="bookstore-link">
                                        <img src="resources/images/bookstore.png" alt="Bookstore" title="Bookstore">
                                    </a>
                                </div>
                                
                            </div>
                        </div> <!-- end section-info-container -->
                        
                        
                        
                        <div class="class-days-container">
                            
                            
                                
                                
                                
                                
                                
                                    
                                        
                                        <div class="row">
                                            
                                            
                                                
                                                
                                                
                                                
                                                
                                                
                                                    
                                                    
                                                    <div class="section-day-time-group push_two five columns">
                                                        
                                                        
                                                            
                                                            
                                                                <span class="section-days">TuTh</span>
                                                                <span class="class-start-time">9:30am</span> - <span class="class-end-time">10:20am</span>
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                        
                                                        
                                                    </div>
                                                    
                                                    
                                                    <div class="section-class-building-group push_one three columns">
                                                        
                                                        <span class="class-building">
                                                            
                                                            
                                                                
                                                                
                                                                
                                                                    <a href="http://www.umd.edu/CampusMaps/bld_detail.cfm?bld_code=MMH" target="_blank"><span class="building-code">MMH</span></a>
                                                                    <span class="class-room">1400</span>
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                            
                                                            
                                                        </span>
                                                        
                                                    </div>
                                                    
                                                
                                                
                                            
                                            
                                            
                                            
                                                
                                                
                                            
                                            
                                        </div> 
                                        
                                    
                                        
                                        <div class="row">
                                            
                                            
                                                
                                                
                                                
                                                
                                                
                                                
                                                    
                                                    
                                                    <div class="section-day-time-group push_two five columns">
                                                        
                                                        
                                                            
                                                            
                                                                <span class="section-days">F</span>
                                                                <span class="class-start-time">11:00am</span> - <span class="class-end-time">11:50am</span>
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                        
                                                        
                                                    </div>
                                                    
                                                    
                                                    <div class="section-class-building-group push_one three columns">
                                                        
                                                        <span class="class-building">
                                                            
                                                            
                                                                
                                                                
                                                                
                                                                    <a href="http://www.umd.edu/CampusMaps/bld_detail.cfm?bld_code=TYD" target="_blank"><span class="building-code">TYD</span></a>
                                                                    <span class="class-room">0102</span>
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                            
                                                            
                                                        </span>
                                                        
                                                    </div>
                                                    
                                                
                                                
                                            
                                            
                                            
                                            
                                                
                                                
                                                    <div class="two columns">
                                                        <span class="class-type">Discussion</span>
                                                    </div>
                                                
                                            
                                            
                                        </div> 
                                        
                                     
                                
                                
                            
                            
                        </div> 
                        
                        
                        
                    </div> 
                
                    <div class="section">
                        
                        <input type="hidden" name="sectionId" value="0106" />
                        
                        <div class="section-info-container">
                            <div class="row">
                                
                                
                                <div class="section-id-container two columns">
                                    
                                    <span class="section-id">
                                        0106
                                    </span>
                                    
                                    
                                    
                                </div>
                                
                                
                                <div class="section-instructors-container six columns">
                                    <span class="section-instructors">
                                        
                                        
                                            
                                            
                                                
                                                
                                                
                                                
                                                    
                                                    
                                                        
                                                            <span class="section-instructor">Katarina Keane</span>
                                                        
                                                        
                                                    
                                                    
                                                
                                                
                                            
                                            
                                            
                                            
                                            
                                        
                                        
                                    </span>
                                </div>
                                
                                
                                <div class="seats-info-group six columns">
                                    <div>
                                        
                                        <span class="section-info-label">Seats</span>
                                        
                                        <span class="seats-info">
                                            
                                            <span class="total-seats">
                                                (<span class="seats-info-label">Total:</span>
                                                <span class="total-seats-count">20</span>,
                                            </span>
                                            
                                            <span class="open-seats ">
                                                <span class="seats-info-label">Open:</span>
                                                <span class="open-seats-count">0</span>,
                                            </span>
                                            
                                            <span class="waitlist ">
                                                <span class="seats-info-label">Waitlist:</span>
                                                <span class="waitlist-count">0</span>)
                                            </span>
                                            
                                        </span>
                                        
                                    </div>
                                </div>
                                
                                
                                <div class="section-action-links-container two columns">
                                    <!--
                                    <a href="#" class="saved-course-section-toggle-link" title="Add to My Saved List">
                                        <input type="hidden" name="courseId" value="HIST289R" />
                                        <input type="hidden" name="sectionId" value="0106" />
                                        <img src="resources/images/unsaved-star.png" />
                                    </a>
                                    -->
                                    <a href="#" class="bookstore-link">
                                        <img src="resources/images/bookstore.png" alt="Bookstore" title="Bookstore">
                                    </a>
                                </div>
                                
                            </div>
                        </div> <!-- end section-info-container -->
                        
                        
                        
                        <div class="class-days-container">
                            
                            
                                
                                
                                
                                
                                
                                    
                                        
                                        <div class="row">
                                            
                                            
                                                
                                                
                                                
                                                
                                                
                                                
                                                    
                                                    
                                                    <div class="section-day-time-group push_two five columns">
                                                        
                                                        
                                                            
                                                            
                                                                <span class="section-days">TuTh</span>
                                                                <span class="class-start-time">9:30am</span> - <span class="class-end-time">10:20am</span>
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                        
                                                        
                                                    </div>
                                                    
                                                    
                                                    <div class="section-class-building-group push_one three columns">
                                                        
                                                        <span class="class-building">
                                                            
                                                            
                                                                
                                                                
                                                                
                                                                    <a href="http://www.umd.edu/CampusMaps/bld_detail.cfm?bld_code=MMH" target="_blank"><span class="building-code">MMH</span></a>
                                                                    <span class="class-room">1400</span>
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                            
                                                            
                                                        </span>
                                                        
                                                    </div>
                                                    
                                                
                                                
                                            
                                            
                                            
                                            
                                                
                                                
                                            
                                            
                                        </div> 
                                        
                                    
                                        
                                        <div class="row">
                                            
                                            
                                                
                                                
                                                
                                                
                                                
                                                
                                                    
                                                    
                                                    <div class="section-day-time-group push_two five columns">
                                                        
                                                        
                                                            
                                                            
                                                                <span class="section-days">F</span>
                                                                <span class="class-start-time">2:00pm</span> - <span class="class-end-time">2:50pm</span>
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                        
                                                        
                                                    </div>
                                                    
                                                    
                                                    <div class="section-class-building-group push_one three columns">
                                                        
                                                        <span class="class-building">
                                                            
                                                            
                                                                
                                                                
                                                                
                                                                    <a href="http://www.umd.edu/CampusMaps/bld_detail.cfm?bld_code=KEY" target="_blank"><span class="building-code">KEY</span></a>
                                                                    <span class="class-room">0119</span>
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                            
                                                            
                                                        </span>
                                                        
                                                    </div>
                                                    
                                                
                                                
                                            
                                            
                                            
                                            
                                                
                                                
                                                    <div class="two columns">
                                                        <span class="class-type">Discussion</span>
                                                    </div>
                                                
                                            
                                            
                                        </div> 
                                        
                                     
                                
                                
                            
                            
                        </div> 
                        
                        
                        
                    </div> 
                
                    <div class="section">
                        
                        <input type="hidden" name="sectionId" value="FC01" />
                        
                        <div class="section-info-container">
                            <div class="row">
                                
                                
                                <div class="section-id-container two columns">
                                    
                                    <span class="section-id">
                                        FC01
                                    </span>
                                    
                                    
                                    
                                </div>
                                
                                
                                <div class="section-instructors-container six columns">
                                    <span class="section-instructors">
                                        
                                        
                                            
                                            
                                                
                                                
                                                
                                                
                                                    
                                                    
                                                        
                                                            <span class="section-instructor">Katarina Keane</span>
                                                        
                                                        
                                                    
                                                    
                                                
                                                
                                            
                                            
                                            
                                            
                                            
                                        
                                        
                                    </span>
                                </div>
                                
                                
                                <div class="seats-info-group six columns">
                                    <div>
                                        
                                        <span class="section-info-label">Seats</span>
                                        
                                        <span class="seats-info">
                                            
                                            <span class="total-seats">
                                                (<span class="seats-info-label">Total:</span>
                                                <span class="total-seats-count">30</span>,
                                            </span>
                                            
                                            <span class="open-seats ">
                                                <span class="seats-info-label">Open:</span>
                                                <span class="open-seats-count">0</span>,
                                            </span>
                                            
                                            <span class="waitlist ">
                                                <span class="seats-info-label">Waitlist:</span>
                                                <span class="waitlist-count">0</span>)
                                            </span>
                                            
                                        </span>
                                        
                                    </div>
                                </div>
                                
                                
                                <div class="section-action-links-container two columns">
                                    <!--
                                    <a href="#" class="saved-course-section-toggle-link" title="Add to My Saved List">
                                        <input type="hidden" name="courseId" value="HIST289R" />
                                        <input type="hidden" name="sectionId" value="FC01" />
                                        <img src="resources/images/unsaved-star.png" />
                                    </a>
                                    -->
                                    <a href="#" class="bookstore-link">
                                        <img src="resources/images/bookstore.png" alt="Bookstore" title="Bookstore">
                                    </a>
                                </div>
                                
                            </div>
                        </div> <!-- end section-info-container -->
                        
                        
                        
                        <div class="class-days-container">
                            
                            
                                
                                
                                
                                
                                
                                    
                                        
                                        <div class="row">
                                            
                                            
                                                
                                                
                                                
                                                
                                                
                                                
                                                    
                                                    
                                                    <div class="section-day-time-group push_two five columns">
                                                        
                                                        
                                                            
                                                            
                                                                <span class="section-days">TuTh</span>
                                                                <span class="class-start-time">6:00pm</span> - <span class="class-end-time">7:15pm</span>
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                        
                                                        
                                                    </div>
                                                    
                                                    
                                                    <div class="section-class-building-group push_one three columns">
                                                        
                                                        <span class="class-building">
                                                            
                                                            
                                                                
                                                                
                                                                
                                                                    <a href="http://www.umd.edu/CampusMaps/bld_detail.cfm?bld_code=KEY" target="_blank"><span class="building-code">KEY</span></a>
                                                                    <span class="class-room">0126</span>
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                                
                                                            
                                                            
                                                        </span>
                                                        
                                                    </div>
                       
                                                    """
                                
                                
course_columns = [
        'code',             # ex. CMSC131
        'title',            # ex. Introduction to Computer Programming via the Web
        'credits',          # ex. 3 credits
        'grade_method',     # ex. REG/P-F/AUD
        'details',          # ex. Corequisite: MATH140 and permission of department...
        'description',      # ex. Introduction to programming and computer science...
        ]
                    
course_pattern = re.compile(r"""
            <div\sclass="course-id">\s*
            (?P<code>.*)<\/div>\s*            
            (<div\sclass="perm-req-message">(?P<permreq>.*?)<\/div>\s*)?
            <\/div>\s*    
            <div\sclass="course-info-container[\w\W\s]+?
            <div\s[\w\W\s]+?
            <div\s[\w\W\s]+?
            <div\s[\w\W\s]+?
            <span\sclass="course-title">(?P<title>[\s\S]*?)<\/span>\s*     
            <\/div>\s*
            <div\s[\w\W\s]+?
            <a\shref[\w\W\s]+?
            <input\s[\w\W\s]+?
            <input\s[\w\W\s]+?
            <img\s[\w\W\s]+?
            <\/a>\s*
            <\/div>\s*
            <\/div>\s*
            <div\s[\w\W\s]+?
            <div\s[\w\W\s]+?
            <div>\s*
            <span\s[\w\W\s]+?<\/span>\s*   
            <span\sclass="course-min-credits">(?P<credits>[\d])<\/span>\s*?
            (?:-\s*<span\sclass="course-max-credits">[\d]<\/span>\s*?)?
            <\/div>\s*?
            <\/div>\s*?
            <div\s[\w\W\s]+?
            <div>\s*?
            <span\s[\w\W\s]+?
            <span\s[\w\W\s]+? 
            <abbr\stitle="Regular[\s\S]*?<span>(?P<grade_method>[\s\S]*?)<\/span><\/abbr>\s*?
            <\/span>\s*
            <\/div>\s*
            <\/div>\s*
            <div\s[\w\W\s]+?
            <div>\s*
            (?:<span\s[\w\W\s]+?<\/span>\s*?
            <a\shref[\w\W\s]+?)?
            <\/div>\s*
            <\/div>\s*
            <div\s[\w\W\s]+?
            <div>\s*
            (?:<span\s[\w\W\s]+?
            <span\s[\w\W\s]+?
            <a\shref[\w\W\s]+?</a></span>)?\s*
            <\/div>\s*?
            <\/div>\s*?
            <\/div>\s*?
            <\/div>\s*?
            (<div\sclass="approved-course-texts-container">\s*?         
            (<div\sclass="row">\s*?
            <div\s[\w\W\s]+?
            <div\sclass="approved-course-text">(?P<details>[\s\S]*?)\s*<\/div>\s*?
            <\/div>\s*?
            <\/div>)?\s*?
            (<div\sclass="row">\s*?
            <div\s[\w\W\s]+?
            <div\sclass="approved-course-text">(?P<description>[\s\S]*?)<\/div>\s*?
            <\/div>\s*?
            <\/div>)?\s*
            <\/div>\s*?                 
            )?\s*?
            <div\sclass="course-texts-container">\s*?
            (<div\sclass="row">\s*?
            <div\s[\w\W\s]+?
            <div\s[\w\W\s]+?<\/div>\s*?
            <\/div>\s*?
            <\/div>\s*?)?
            <\/div>       
            """, re.IGNORECASE | re.VERBOSE)

text = re.findall(course_pattern, target)
courses = list()

for m in course_pattern.finditer(target):
            course_raw_data = m.groupdict()
            course = dict()
            for col in course_columns:
                course[col] = clean_and_trim(course_raw_data[col])
                print(course[col])
            print("\n")
            courses.append(course)


