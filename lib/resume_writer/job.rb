# ftl_resume/job.rb

module ResumeWriter
  class Job
    attr_accessor :end_date, :employer, :extra, :start_date, :tech, :title
    attr_accessor :blurb

    def initialize(data = {})
      @data = data
      parse_data
    end

    def parse_data
      @start_date   = @data.fetch(:start_date, 1961)
      @end_date     = @data.fetch(:end_date, 2071)
      @title        = @data.fetch(:title, 'Great guy')
      @employer     = @data.fetch(:employer, 'God')
      @blurb        = @data.fetch(:blurb, nil)
      @tech         = @data.fetch(:tech, nil)
      @extra        = @data.fetch(:extra, nil)
    end

    def to_h
      job = Hash.new
      job[:start_date] = @start_date
      job[:end_date]   = @end_date
      job[:title]      = @title
      job[:employer]   = @employer
      job[:blurb]      = @blurb
      job[:tech]       = @tech
      job[:extra]      = @extra
      job
    end
  end

end
