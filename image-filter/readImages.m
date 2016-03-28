srcFiles = dir('/Users/siddeshpillai/Desktop/blah/images/*.jpg');  % the folder in which ur images exists
for i = 1 : length(srcFiles)
    filename = strcat('/Users/siddeshpillai/Desktop/blah/images/',srcFiles(i).name);

    % read images
    I = imread(filename);
    
    % Gaussian Filter
    gaussian = imgaussfilt(I,10);
    imwrite(gaussian, strcat(filename,'_gauss.jpg'));

    % Complement Filter
    complement = imcomplement(I);
    imwrite(complement, strcat(filename, '_complement.jpg'));

    % Bright Filter
    bright = imadjust(I ,[.2 .3 0; .6 .7 1],[]);
    imwrite(bright, strcat(filename, '_bright.jpg'));

    %Low light Filter
    low = imadjust(I ,[.8 .4 0; .9 .8 1],[]);
    imwrite(low, strcat(filename, '_low.jpg'));

end