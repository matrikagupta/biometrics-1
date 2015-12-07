function out=load_database(force_load);
% We load the database the first time we run the program.
persistent unsignedTrainSet;
persistent loaded
if force_load == 1
    loaded = [];
end

if(isempty(loaded))

    % @TODO: Fix Size.
    % @TODO: Dynamic Count Images.
    trainSet=zeros(67600,400);
    %% Getting path of each user train images
    trainFolderPath = '../training_images';
    trainFolderList = dir(trainFolderPath);
    trainFolderList = trainFolderList(~strncmpi('.', {trainFolderList.name}, 1));
    %% Iterating on training user list.
    for p = 1 : length(trainFolderList)
        userFolder = trainFolderList(p).name;
        userImagesList = dir(strcat(trainFolderPath, '/', userFolder, '/*.pgm'));
        %% Iterating on images for each user.
        for q = 1 : length(userImagesList)
            userImage=imread(strcat(trainFolderPath, '/', userFolder, '/', userImagesList(q).name));
            trainSet(:,(p-1)*10+q)=reshape(userImage,size(userImage,1)*size(userImage,2),1);
        end
    end
    % cd ..

    %         cd(strcat('s',num2str(i)));
    %         for j=1:10
    %             a=imread(strcat(num2str(j),'.pgm'));
    %             trainSet(:,(i-1)*10+j)=reshape(a,size(a,1)*size(a,2),1);
    %         end

    unsignedTrainSet=uint8(trainSet); % Convert to unsigned 8 bit numbers to save memory.
end

loaded=1;  % Set 'loaded' to aviod loading the database again.
out=unsignedTrainSet;